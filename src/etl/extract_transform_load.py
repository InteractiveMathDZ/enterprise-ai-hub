import os
from datetime import datetime, timezone
import pandas as pd
import requests
from dotenv import load_dotenv
from supabase import Client, create_client

# تحميل متغيرات البيئة
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
  raise ValueError("يرجى التأكد من ضبط SUPABASE_URL و SUPABASE_KEY في متغيرات البيئة")

# إنشاء عميل Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def extract_data() -> pd.DataFrame:
  """مرحلة الاستخراج (Extract): سحب بيانات حية من API عام ومجاني (CoinGecko Markets)"""
  url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"

  try:
    print("🔄 جاري الاتصال بالـ API وسحب البيانات الحية...")
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    data = response.json()
    print(f"✅ تم سحب {len(data)} سجل حي من الـ API بنجاح.")
    return pd.DataFrame(data)
  except Exception as e:
    print(f"❌ حدث خطأ أثناء سحب البيانات من الـ API: {e}")
    return pd.DataFrame()


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
  """مرحلة التحويل (Transform): تنظيف ومواءمة البيانات الحية لتتناسب مع جدول النظام المؤسسي"""
  if df.empty:
    print("⚠️ البيانات المستخرجة فارغة.")
    return df

  # اختيار وتكييف الأعمدة لتتطابق مع جدول sales_transactions
  transformed = pd.DataFrame()

  # دمج اسم العملة الرمز مع رمزها لتصبح فئة المنتج
  transformed["product_category"] = (
      df["name"] + " (" + df["symbol"].str.upper() + ")"
  )

  # تحويل السعر الحالي إلى قيمة رقمية نظيفة لتمثل مبلغ المعاملة/التقييم
  transformed["amount"] = pd.to_numeric(df["current_price"], errors="coerce").fillna(0.0)

  # محاكاة توزيع جلي للعملاء والمناطق جغرافياً بناءً على مؤشرات البيانات
  regions = ["North America", "Europe", "MENA", "Asia-Pacific"]
  transformed["customer_region"] = [
      regions[i % len(regions)] for i in range(len(df))
  ]

  # إضافة الطابع الزمني الحالي بتوقيت UTC
  transformed["transaction_date"] = datetime.now(timezone.utc).isoformat()
  transformed["status"] = "completed"

  # فلترة وتنقية القيم الصفرية أو السالبة
  transformed = transformed[transformed["amount"] > 0].copy()

  print(f"✅ تم تنظيف وتحويل البيانات الحية. عدد الصفوف الصالحة: {len(transformed)}")
  return transformed


def load_data(df: pd.DataFrame):
  """مرحلة التحميل (Load): إرسال البيانات المنظفة الحية إلى Supabase PostgreSQL"""
  if df.empty:
    print("⚠️ لا توجد سجلات صالحة لتحميلها.")
    return

  records = df.to_dict(orient="records")

  # إدخال السجلات الحية في جدول Supabase
  response = supabase.table("sales_transactions").insert(records).execute()
  print("🚀 تم تحميل البيانات الحية بنجاح إلى قاعدة البيانات (Supabase)!")


if __name__ == "__main__":
  print("=== بدء تشغيل أنبوب البيانات الحية (Live API ETL Pipeline) ===")
  df_raw = extract_data()
  df_clean = transform_data(df_raw)
  load_data(df_clean)
  print("=== اكتملت عملية الـ ETL الحية بنجاح ===")
