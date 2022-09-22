<img src="https://img.shields.io/github/license/TralahM/pyflexpay"> <img src="https://img.shields.io/github/last-commit/TralahM/pyflexpay"> <img src="https://img.shields.io/github/contributors/TralahM/pyflexpay"> <img src="https://img.shields.io/github/issues-pr-raw/TralahM/pyflexpay?color=blue"> <img src="https://img.shields.io/github/issues-pr-closed-raw/TralahM/pyflexpay?color=red"> <img src="https://img.shields.io/github/issues-raw/TralahM/pyflexpay?color=green">
<img src="https://img.shields.io/github/issues-closed-raw/TralahM/pyflexpay?color=yellow"> <img src="https://img.shields.io/github/forks/TralahM/pyflexpay?label=Forks&style=social"> <img src="https://img.shields.io/github/forks/TralahM/pyflexpay?label=Forks&style=social"> <img src="https://img.shields.io/github/stars/TralahM/pyflexpay?style=social">
<img src="https://img.shields.io/github/watchers/TralahM/pyflexpay?label=Watch&style=social"> <img src="https://img.shields.io/github/downloads/TralahM/pyflexpay/total"> <img src="https://img.shields.io/github/repo-size/TralahM/pyflexpay"> <img src="https://img.shields.io/github/languages/count/TralahM/pyflexpay"> <img src="https://img.shields.io/github/v/tag/TralahM/pyflexpay"> <img src="https://img.shields.io/readthedocs/pyflexpay"> <img src="https://img.shields.io/pypi/v/pyflexpay"> <img src="https://img.shields.io/pypi/pyversions/pyflexpay"> <img src="https://img.shields.io/pypi/wheel/pyflexpay"> <img src="https://img.shields.io/pypi/status/pyflexpay?label=pypi%20status"> <img src="https://img.shields.io/pypi/format/pyflexpay?label=pypi%20format">

# pyflexpay
> A Python SDK for the FlexPay API used by Corporate Merchants to
> connect to FlexPay to perform mobile money transactions.

The FlexPay API provides access to two interfaces, the interface for sending
the request (Payment Service) and that for verifying the
transaction (Check transaction).

### Table of Contents
- [Payment Service](#Payment-Service)
- [Check Transaction](#Check-transaction)
- [QuickStart](#QuickStart)
- [Documentation/Usage](#Documentation)
- [Contributing](#Contributing)
- [Credits](#Credits)

---

## Payment Service
This service is used to send a payment request to FlexPay
- URL: https://ip:port/api/rest/v1/paymentService
- Method: POST
- Format: JSON

### Request
![](payment_service_request_params.png)


### Response
![](payment_service_response_params.png)


### Result
![](payment_service_result.png)

### Example
![](payment_service_example.png)

## Check transaction
This service is used to check the status of a payment request previously sent to FlexPay.
- URL: http://ip:port/api/rest/v1/check/orderNumber
- Method: GET

### Request
![](check_transaction_request_params.png)


### Response
![](check_transaction_response_params.png)


### Example
![](check_transaction_example.png)

---

## QuickStart
#### Installation

```
pip install pyflexpay
```
#### From Source
```
git clone https://github.com/TralahM/pyflexpay
cd pyflexpay

python setup.py bdist_wheel
pip install -e .

```
---

## Documentation

[![Documentation](https://img.shields.io/badge/Docs-pyflexpay-blue.svg?style=for-the-badge)](https://pyflexpay.readthedocs.io)


#### API Reference

---
## Contributing

---

## Credits
[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)



[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-blue?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-white.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.github.io)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://github.com/tralahtek)
---
