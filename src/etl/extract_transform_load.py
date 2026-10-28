import os
import pandas as pd
from datetime import datetime, timezone
from dotenv import load_dotenv
from supabase import create_client, Client

# تحميل متغيرات البيئة (تعمل محلياً أو تأتي من GitHub Actions Secrets)
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("يرجى التأكد من ضبط SUPABASE_URL و SUPABASE_KEY في متغيرات البيئة")

# إنشاء عميل Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def extract_data() -> pd.DataFrame:
    """مرحلة الاستخراج (Extract): محاكاة جلب بيانات سريعة من مصدر خارجي أو محلي"""
    raw_data = [
        {
            "date": "2026-10-25T10:30:00Z",
            "region": "North America",
            "category": "Cloud Services",
            "amount": "1500.50",
            "status": "completed",
        },
        {
            "date": "2026-10-25T11:15:00Z",
            "region": "Europe",
            "category": "AI Subscriptions",
            "amount": "299.00",
            "status": "completed",
        },
        {
            "date": "2026-10-26T08:00:00Z",
            "region": "MENA",
            "category": "Data Pipeline Setup",
            "amount": "4500.00",
            "status": "completed",
        },
        {
            "date": "2026-10-26T09:45:00Z",
            "region": "Europe",
            "category": "Cloud Services",
            "amount": " - ",  # قيمة غير نظيفة للمعايرة
            "status": "pending",
        },
    ]
    print("✅ تم استخراج البيانات الخام بنجاح.")
    return pd.DataFrame(raw_data)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """مرحلة التحويل (Transform): تنظيف البيانات وإعدادها للتخزين"""
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0.0)
    df = df[df["amount"] > 0].copy()
    df.rename(
        columns={
            "date": "transaction_date",
            "region": "customer_region",
            "category": "product_category",
        },
        inplace=True,
    )
    print(f"✅ تم تنظيف وتحويل البيانات. عدد الصفوف الصالحة: {len(df)}")
    return df

def load_data(df: pd.DataFrame):
    """مرحلة التحميل (Load): إرسال البيانات المغسولة إلى Supabase PostgreSQL"""
    records = df.to_dict(orient="records")
    if not records:
        print("⚠️ لا توجد سجلات جديدة لتحميلها.")
        return
    response = supabase.table("sales_transactions").insert(records).execute()
    print("🚀 تم تحميل البيانات بنجاح إلى قاعدة البيانات (Supabase)!")

if __name__ == "__main__":
    print("=== بدء تشغيل أنبوب البيانات (ETL Pipeline) السحابي ===")
    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)
    print("=== اكتملت عملية الـ ETL بنجاح ===")
