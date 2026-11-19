def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature


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


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("All tests completed - program didn't crash!")
