def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if 0 <= temperature <= 40:
        return temperature
    elif temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        result = input_temperature("25")
        print(f"Temperature is now {result}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is '100'")
    try:
        result = input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
