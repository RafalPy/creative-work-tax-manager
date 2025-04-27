# CREATIVE WORK TAX MANAGER
# To run the app:
# flask --app app run --debug
### docker compose up

#Sample insert: 
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Sample Evidence\",\"description\":\"This is a sample description.\",\"date\":\"2025-04-27\"}" http://127.0.0.1:5000/evidence/