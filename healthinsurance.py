class HealthInsurancePremiumCalculator:
    def __init__(self, base_premium_rate=1000):
        self.base_premium_rate = base_premium_rate

    def calculate_premium(self, age, gender, coverage_type, health_conditions=None):
        # Base premium based on age and gender
        base_premium = self.calculate_base_premium(age, gender)

        # Adjust premium based on coverage type
        coverage_premium = self.calculate_coverage_premium(coverage_type)

        # Consider additional health-related parameters
        additional_premium = self.calculate_additional_premium(health_conditions)

        # Total premium calculation
        total_premium = base_premium + coverage_premium + additional_premium

        return total_premium

    def calculate_base_premium(self, age, gender):
        # Basic premium calculation based on age and gender
        gender_factor = 1.2 if gender.lower() == 'male' else 1.1
        base_premium = self.base_premium_rate * age * gender_factor

        return base_premium

    def calculate_coverage_premium(self, coverage_type):
        # Premium adjustment based on coverage type
        if coverage_type.lower() == 'basic':
            coverage_premium = 0.05 * self.base_premium_rate
        elif coverage_type.lower() == 'comprehensive':
            coverage_premium = 0.1 * self.base_premium_rate
        else:
            coverage_premium = 0

        return coverage_premium

    def calculate_additional_premium(self, health_conditions):
        # Additional premium based on specific health conditions
        additional_premium = 0

        if health_conditions:
            # Adjust premium based on specific health conditions
            for condition, condition_factor in self.get_condition_factors().items():
                user_input = input(
                    f"Do you have {condition.replace('_', ' ')}? (Enter 'True' or 'False'): ").lower()
                health_conditions[condition] = True if user_input == 'true' else False

                if health_conditions[condition]:
                    additional_premium += condition_factor * self.base_premium_rate

        return additional_premium

    def get_condition_factors(self):
        # Define factors for specific health conditions
        condition_factors = {
            'diabetes': 0.2,
            'cancer': 0.3,
            'smoker': 0.15,
            'alcohol_consumer': 0.1,
            'hereditary_problem': 0.25,
            'heart_patient': 0.3,
            'asthma': 0.2,
            'thyroid': 0.15,
            'tb': 0.25,
            'anaemic': 0.1,
            # Add more conditions and factors as needed
        }

        return condition_factors


def get_user_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            if input_type == 'boolean':
                return True if user_input.lower() == 'true' else False
            elif input_type == 'numeric':
                return float(user_input)
            else:
                raise ValueError("Invalid input type specified.")
        except ValueError:
            print("Invalid input. Please enter the correct type of input.")


def main():
    print("Welcome to the Health Insurance Premium Calculator!")

    # Input parameters
    age = get_user_input("Enter your age: ", 'numeric')
    gender = input("Enter your gender (Male/Female): ")
    coverage_type = input("Enter coverage type (Basic/Comprehensive): ").lower()
    health_conditions = {}

    print("\nEnter 'True' if you have the following conditions; otherwise, enter 'False'.")

    # Gather health-related parameters
    for condition in calculator.get_condition_factors():
        health_conditions[condition] = get_user_input(f"Do you have {condition.replace('_', ' ')}? ", 'boolean')

    # Calculate premium
    premium = calculator.calculate_premium(age, gender, coverage_type, health_conditions)

    # Output the premium
    print(f"\nThe health insurance premium is {premium} rupees per month.")


# Example usage:
calculator = HealthInsurancePremiumCalculator()
main()
