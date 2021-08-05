# Tom's calculator

The test assignment for NDA company

## Task

Tom, an owner of a small grocery store asks for help.
Last year, Tom started his own business in a small town and he has to do everything himself, including sitting at the checkout. Now he is counting
the cost of the order manually, which is very inconvenient, since taxes and discount must be taken into account.
To make matters worse, Tom has recently expanded to other states, and now he needs to take into account
calculating taxes of other states.
After a little thought, he came to the conclusion that he needed an application with
simple user interface, three input fields and one output field of the final cost of the order.

How should it work:

- A discount is calculated based on the total order value and
the discounted price is displayed.

- Then state tax is added based on state code and price
with a discount and the total cost is displayed, taking into account
discount and added tax.

### Default taxes and discounts

|Order Price, USD| Discount, % | State Alpha Code | Tax, % |
| --- | --- | --- | --- |
| >= 1000 | 3 | UT | 6.85 |
| >= 5000 | 5 | NV | 8 |
| >= 7000 | 7 | TX | 6.25 |
| >= 10000 | 10 | AL | 4 |
| >= 50000 | 15 | CA | 8.25 |

> BTW one can change default values in `backend/config.toml`

## How to run

```bash
docker-compose build
docker-compose up
```

By default UI would be accessible at `localhost:8080` and Backend OpenAPI at `localhost:8000/oas`

## Tests


```bash
cd backend
# install dependencies
poetry install
ward
```
