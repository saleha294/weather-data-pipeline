# Take the clean data and save it into the database.

from database import get_database_connection


def load_weather_data(cleaned_weather_data):

    connection = get_database_connection()  # Connect me to PostgreSQL.

    if connection is None:
        print("Connection is none.")
        return

    cursor = connection.cursor()  # Give me something that can execute SQL.

    query = """
    INSERT INTO weather (
        temperature,
        humidity,
        wind_speed,
        time_stamp,
        city
    )
    VALUES (
        %s, %s, %s, %s, %s
    )
    """

    values_list = [
        cleaned_weather_data.get("temperature"),
        cleaned_weather_data.get("humidity"),
        cleaned_weather_data.get("wind_speed"),
        cleaned_weather_data.get("time"),
        cleaned_weather_data.get("city")
    ]

    try:
        cursor.execute(query, values_list)
        connection.commit()
        print("Data loaded sucessfully in the database.")

    except:
        print("Error")
        return None

    finally:
        cursor.close()
        connection.close()