class PatternGenerator:
    def __init__(self, increments):
        """
        Initialize the pattern generator with a specific increment pattern.
        """
        self.increments = increments

    def generate_output(self, input_array):
        """
        Generate the output array by applying position-based increments.
        """
        output_array = []
        for i, value in enumerate(input_array):
            increment = self.increments[i % len(self.increments)]
            output_array.append(value + increment)
        return output_array


increment_pattern = [3, 4, 2]


generator = PatternGenerator(increment_pattern)


input_arrays = [
    [1, 2, 3],
    [5, 5, 5],
    [2, 3, 5],
    [1, 1, 1]
]


for input_array in input_arrays:
    output = generator.generate_output(input_array)
    print(f"Input: {input_array} -> Output: {output}")
