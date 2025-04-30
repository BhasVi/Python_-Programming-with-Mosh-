has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
    print("Eligible for Loan")

if has_good_credit or has_high_income:
    print("Eligible for Loan")

has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for Loan")