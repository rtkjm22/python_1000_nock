def calc_monthly_income(annual_income: int) -> int:
    return annual_income // 12


if __name__ == "__main__":
    try:
        income_str = input(">>> ")
        annual_income = int(income_str)
        monthly_income = calc_monthly_income(annual_income)
        print(f"月収はおよそ ¥{monthly_income:,}です。")
    except ValueError:
        print("※ 数字だけ入力してください。")
    except ZeroDivisionError:
        print("※ 年収がゼロの場合は計算できません。")
    except Exception as e:
        print(f"予測不能なエラーです: {e}")
