import numpy as np
import matplotlib.pyplot as plt
import nistrng
from copy import copy
from scipy.stats import entropy
import nistrng


def assemble_bits(bitstring, bits=8):
    output = []
    for i in range(len(bitstring) // bits):
        output.append(int("".join(bitstring[i * bits : (i + 1) * bits].astype(str)), 2))
    return np.array(output)


def calculate_entropy(bitstring, type):
    if type == "bits":
        base = 2
        arr = bitstring
    elif type == "bytes":
        base = 256
        arr = assemble_bits(bitstring)
    else:
        raise ValueError("Wrong type")

    propor = np.unique(arr, return_counts=True)
    return entropy(propor[1] / len(arr), base=base)


def draw_distribution(bitstring, bits=8):
    bytes_ = assemble_bits(bitstring, bits=bits)
    plt.hist(bytes_, bins=np.arange(max(bytes_) + 2))
    plt.show()


def nist_tests(bitstring):
    # Check the eligibility of the test and generate an eligible battery from the default NIST-sp800-22r1a battery
    eligible_battery: dict = nistrng.check_eligibility_all_battery(
        bitstring, nistrng.SP800_22R1A_BATTERY
    )
    length = len(bitstring)
    # Print the eligible tests
    print("Eligible test from NIST-SP800-22r1a:")

    tests = copy(list(eligible_battery.keys()))
    for name in tests:
        if name in ["monobit", "frequency_within_block", "runs", "cumulative sums"]:
            if length < 100:
                del eligible_battery[name]
        elif name == "dft":
            if length < 1000:
                del eligible_battery[name]
        elif name in ["random_excursion", "random_excursion_variant"]:
            if length < int(1e6):
                del eligible_battery[name]

    for name in eligible_battery.keys():
        print("-" + name)
    # Test the result on the eligible tests
    results = nistrng.run_all_battery(bitstring, eligible_battery, False)
    # Print results one by one
    print("Test results:")
    failed = 0
    for result, elapsed_time in results:
        if result.passed:
            print(
                "- PASSED - score: "
                + str(np.round(result.score, 3))
                + " - "
                + result.name
                + " - elapsed time: "
                + str(elapsed_time)
                + " ms"
            )
        else:
            failed += 1
            print(
                "- FAILED - score: "
                + str(np.round(result.score, 3))
                + " - "
                + result.name
                + " - elapsed time: "
                + str(elapsed_time)
                + " ms"
            )

    print(f"Total failed tests: {failed}/{len(eligible_battery.keys())}")
