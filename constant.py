class PayScale(enum.Enum):
    FLAT_FEE = 'joining_flat'
    HIGHER_OF_FEE = 'joining_higher'
    LOWER_OF_FEE = 'joining_lower'
    PERCENTAGE_WITH_RANGE = 'joining_range'
