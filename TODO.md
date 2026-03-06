
# E-Commerce API - TODO

## 1. AUTH `/auth`
- [ 
] POST `/auth/register` — yangi foydalanuvchi ro'yxatdan o'tkazish
- [ ] POST `/auth/login` — email/password bilan kirish, access + refresh token qaytaradi
- [ ] POST `/auth/refresh` — refresh token bilan yangi access token olish
- [ ] POST `/auth/logout` — refresh tokenni blacklistga qo'shish
- [ ] GET  `/auth/google` — Google OAuth sahifasiga yo'naltirish
- [ ] GET  `/auth/google/callback` — Google dan qaytgandan keyin token berish
- [ ] POST `/auth/forgot-password` — email ga reset link yuborish
- [ ] POST `/auth/reset-password` — yangi parol o'rnatish

---

## 2. USERS `/users`
- [ ] GET    `/users/me` — o'z profilini ko'rish
- [ ] PATCH  `/users/me` — o'z profilini tahrirlash (username, full_name, avatar)
- [ ] DELETE `/users/me` — o'z akkauntini o'chirish

### Admin
- [ ] GET    `/users` — barcha foydalanuvchilar ro'yxati (pagination)
- [ ] GET    `/users/{id}` — bitta foydalanuvchi ma'lumoti
- [ ] PATCH  `/users/{id}` — foydalanuvchini tahrirlash (is_active, is_admin)
- [ ] DELETE `/users/{id}` — foydalanuvchini o'chirish

---

## 3. CATEGORIES `/categories`
- [ ] GET    `/categories` — barcha kategoriyalar ro'yxati
- [ ] GET    `/categories/{id}` — bitta kategoriya va uning ichidagilari

### Admin
- [ ] POST   `/categories` — yangi kategoriya yaratish
- [ ] PATCH  `/categories/{id}` — kategoriyani tahrirlash
- [ ] DELETE `/categories/{id}` — kategoriyani o'chirish

---

## 4. PRODUCTS `/products`
- [ ] GET  `/products` — mahsulotlar ro'yxati (pagination, filter, search)
  - query params: `page`, `limit`, `category_id`, `min_price`, `max_price`, `search`, `sort`
- [ ] GET  `/products/{id}` — bitta mahsulot to'liq ma'lumoti

### Admin
- [ ] POST   `/products` — yangi mahsulot qo'shish
- [ ] PATCH  `/products/{id}` — mahsulotni tahrirlash
- [ ] DELETE `/products/{id}` — mahsulotni o'chirish

---

## 5. CART `/cart`
- [ ] GET    `/cart` — o'z savatini ko'rish
- [ ] POST   `/cart/items` — savatga mahsulot qo'shish `{ product_id, quantity }`
- [ ] PATCH  `/cart/items/{item_id}` — savatdagi mahsulot sonini o'zgartirish
- [ ] DELETE `/cart/items/{item_id}` — savatdan mahsulotni o'chirish
- [ ] DELETE `/cart` — savatni to'liq tozalash

---

## 6. ADDRESSES `/addresses`
- [ ] GET    `/addresses` — o'z manzillar ro'yxati
- [ ] POST   `/addresses` — yangi manzil qo'shish
- [ ] PATCH  `/addresses/{id}` — manzilni tahrirlash
- [ ] DELETE `/addresses/{id}` — manzilni o'chirish
- [ ] PATCH  `/addresses/{id}/default` — manzilni default qilish

---

## 7. ORDERS `/orders`
- [ ] GET  `/orders` — o'z orderlari ro'yxati
- [ ] GET  `/orders/{id}` — bitta order to'liq ma'lumoti
- [ ] POST `/orders` — savatdan yangi order yaratish `{ address_id }`
- [ ] POST `/orders/{id}/cancel` — orderni bekor qilish (faqat pending holatda)

### Admin
- [ ] GET   `/orders` — barcha orderlar (filter: status, user_id, date)
- [ ] PATCH `/orders/{id}/status` — order statusini o'zgartirish

---

## 8. PAYMENTS `/payments`
- [ ] POST `/payments/checkout/{order_id}` — Stripe payment intent yaratish
- [ ] POST `/payments/webhook` — Stripe webhook (to'lov muvaffaqiyatli bo'lganda orderni paid ga o'tkazish)
- [ ] GET  `/payments/{order_id}` — order to'lov ma'lumoti

---

## Keyingi bosqichlar (optional)
- [ ] Mahsulot rasmlari upload qilish (AWS S3 yoki Cloudinary)
- [ ] Email yuborish (register, order confirm, reset password)
- [ ] Review — mahsulotga baho berish
- [ ] Coupon — chegirma kodlari
- [ ] Rate limiting — spam himoyasi
- [ ] Redis — token blacklist va cache uchun