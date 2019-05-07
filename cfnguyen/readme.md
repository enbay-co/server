a client

payment link  pcode

1/ merchant request a pc
curl -X POST \
  http://localhost:1234/pc \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Host: localhost:1234' \
  -d '{
	"bill_id": "bill123",
	"price":  "100000",
	"callback_url": "http://localhost:5000/bill"
}'

2/ customer scan for payment
curl -X GET \
  http://localhost:1234/pc/222iks42 \
  -H 'Accept: */*' \
  -H 'Host: localhost:1234' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache'

3/ enbay request to merchant to get bill 
curl -X GET \
  http://localhost:5000/bill/bill123 \
  -H 'Accept: */*' \
  -H 'Host: localhost:5000' \
  -H 'cache-control: no-cache'