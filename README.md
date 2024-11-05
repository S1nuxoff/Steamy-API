# Steamy API

## Description

**Steamy API** is a comprehensive API designed to manage users, handle items, and seamlessly integrate with the Steam platform. It allows you to create and update users, manage their favorite items, and retrieve detailed information about Steam users and items.

## Features

- **User Management**: Create, update, and manage users and their favorite items.
- **Steam Integration**: Retrieve information about Steam users, including their statistics, achievements, games, and more.
- **Item Handling**: Access detailed information about item prices, sales history, liquidity, and other characteristics.
- **Security**: Authenticate requests using API keys to ensure secure access.

## Getting Started

### Requirements

- **Python 3.8+**
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Uvicorn**: A lightning-fast ASGI server for Python.
- **Other dependencies**: Listed in the `requirements.txt` file.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/S1nuxoff/Steamy-API
   cd steamy-api
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scriptsctivate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file and add the necessary variables, for example:

   ```env
   API_KEY=your_api_key
   DATABASE_URL=your_database_url
   ```

5. **Run the Server:**

   ```bash
   uvicorn main:app --reload
   ```

   The server will be available at `http://localhost:8000`.

## Documentation

FastAPI automatically generates interactive documentation for your API, accessible at the following routes:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-docs.png)  
_Example Swagger UI Interface_

## Authentication

The API uses API keys to authenticate requests. You must include your API key in the `X-API-KEY` header of each request.

### Example Request Using `curl`:

```bash
curl -H "X-API-KEY: your_api_key" "http://localhost:8000/api/v1/user/?tg_id=123456"
```

## Endpoints

### User

- **GET `/api/v1/user/`**  
  Retrieve a user by Telegram ID.

  **Query Parameters:**

  - `tg_id` (integer, required): Telegram ID of the user.

- **GET `/api/v1/user/favorites`**  
  Retrieve a user's favorite items.

  **Query Parameters:**

  - `tg_id` (integer, required): Telegram ID of the user.
  - `game` (string, optional): Name of the game.

- **POST `/api/v1/user/create`**  
  Create a new user.

  **Request Body:**

  ```json
  {
    "tg_id": 123456,
    "username": "example_user",
    "language": "en"
  }
  ```

- **PATCH `/api/v1/user/update`**  
  Update user information.

  **Query Parameters:**

  - `tg_id` (integer, required): Telegram ID of the user.

  **Request Body:**

  ```json
  {
    "username": "new_username",
    "steam_id": 789012,
    "premium": true,
    "language": "ru",
    "currency": "USD",
    "game": "CS:GO"
  }
  ```

- **POST `/api/v1/user/add_favorite`**  
  Add an item to favorites.

  **Query Parameters:**

  - `tg_id` (integer, required): Telegram ID of the user.

  **Request Body:**

  ```json
  {
    "item": "AK-47",
    "game": "CS:GO"
  }
  ```

- **DELETE `/api/v1/user/remove_favorite`**  
  Remove an item from favorites.

  **Query Parameters:**

  - `tg_id` (integer, required): Telegram ID of the user.

  **Request Body:**

  ```json
  {
    "item": "AK-47",
    "game": "CS:GO"
  }
  ```

### Items

- **GET `/api/v1/items/`**  
  Retrieve item information by name.

  **Query Parameters:**

  - `market_hash_name` (string, required): Name of the item on the market.

### Steam User

- **GET `/api/v1/steam/user/search`**  
  Search for a Steam user by ID.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/stats`**  
  Retrieve Steam user statistics.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.
  - `appid` (integer, required): Application (game) ID.

- **GET `/api/v1/steam/user/wishlist`**  
  Retrieve a Steam user's wishlist.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/bans`**  
  Retrieve Steam user ban information.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/badges`**  
  Retrieve Steam user badges.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/recently_played_games`**  
  Retrieve recently played games of a Steam user.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/friends`**  
  Retrieve a Steam user's friends list.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/details`**  
  Retrieve detailed information about a Steam user.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/level`**  
  Retrieve a Steam user's level.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/achievements`**  
  Retrieve a Steam user's achievements.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

- **GET `/api/v1/steam/user/owned_games`**  
  Retrieve a Steam user's owned games list.

  **Query Parameters:**

  - `steam_id` (integer, required): Steam ID of the user.

### Steam Item

- **GET `/api/v1/steam/item/price`**  
  Retrieve the price of an item in the specified currency.

  **Query Parameters:**

  - `game` (string, required): Name of the game.
  - `item` (string, required): Name of the item.
  - `currency` (string, required): Currency.

- **GET `/api/v1/steam/item/sales`**  
  Retrieve the sales history of an item.

  **Query Parameters:**

  - `currency` (string, required): Currency.
  - `game` (string, required): Name of the game.
  - `item` (string, required): Name of the item.
  - `period` (string, optional): Period (`day`, `week`, `month`, `lifetime`). Default is `week`.

- **GET `/api/v1/steam/item/liquidity`**  
  Retrieve the liquidity of an item.

  **Query Parameters:**

  - `nameid` (integer, required): Item ID.

- **GET `/api/v1/steam/item/markets_prices`**  
  Retrieve market prices for an item.

  **Query Parameters:**

  - `game` (string, required): Name of the game.
  - `item` (string, required): Name of the item.
  - `currency` (string, required): Currency.

- **GET `/api/v1/steam/item/float`**  
  Retrieve the float value of an item.

  **Query Parameters:**

  - `rungame_url` (string, required): Game URL.

- **GET `/api/v1/steam/item/nameid`**  
  Retrieve the Nameid of an item.

  **Query Parameters:**

  - `game` (string, required): Name of the game.
  - `item` (string, required): Name of the item.

### Root

- **GET `/`**  
  Root endpoint that returns a welcome message.

## Data Schemas

### User

```json
{
  "id": integer,
  "steam_id": integer | null,
  "premium": boolean,
  "language": string,
  "currency": string,
  "game": string
}
```

### UserCreate

```json
{
  "tg_id": integer,
  "username": string,
  "language": string
}
```

### UserUpdate

```json
{
  "username": string | null,
  "steam_id": integer | null,
  "premium": boolean | null,
  "language": string | null,
  "currency": string | null,
  "game": string | null
}
```

### UserAddFavorite

```json
{
  "item": string,
  "game": string
}
```

### UserRemoveFavorite

```json
{
  "item": string,
  "game": string
}
```

### FavouriteResponse

```json
{
  "id": integer,
  "user_id": integer,
  "item": string,
  "game": string,
  "added_at": "2023-10-10T10:00:00Z"
}
```

### Item

```json
{
  "nameid": integer,
  "hash_name": string,
  "game": integer,
  "id": integer
}
```

### HTTPValidationError

```json
{
  "detail": [
    {
      "loc": ["query", "tg_id"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### ValidationError

```json
{
  "loc": ["body", "username"],
  "msg": "field required",
  "type": "value_error.missing"
}
```

## Usage Examples

### Create a User

**Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/user/create" -H "Content-Type: application/json" -H "X-API-KEY: your_api_key" -d '{
  "tg_id": 123456,
  "username": "example_user",
  "language": "en"
}'
```

**Response:**

```json
{
  "id": 1,
  "steam_id": null,
  "premium": false,
  "language": "en",
  "currency": "USD",
  "game": "CS:GO"
}
```

### Retrieve User Information

**Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/user/?tg_id=123456" -H "X-API-KEY: your_api_key"
```

**Response:**

```json
{
  "id": 1,
  "steam_id": 789012,
  "premium": true,
  "language": "ru",
  "currency": "USD",
  "game": "CS:GO"
}
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to contact us at [v.schip4@gmail.com](mailto:v.schip4@gmail.com).

---

_This README was automatically generated based on the provided OpenAPI specification._
