# استخدام Python الرسمي
FROM python:3.12-slim-bullseye

# جعل الإخراج مباشرًا دون تخزين مؤقت
ENV PYTHONUNBUFFERED=1

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# تثبيت المتطلبات فقط أولاً لتقليل إعادة بناء الصورة
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع بعد تثبيت المكتبات
COPY . .

# تشغيل التطبيق عند تشغيل الحاوية
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
