from itertools import chain, combinations

def power_set(A):
    """
    Skilar veldismengi mengisins A.
    Veldismengi er mengi allra hlutmengja af A, þar á meðal tóma mengið og A sjálft.
    """
    return list(chain.from_iterable(combinations(A, r) for r in range(len(A) + 1)))

def is_subset(subset, set_):
    """
    Athugar hvort fyrsta mengið (subset) sé hlutmengi af seinna menginu (set_).
    Skilar True ef subset er hlutmengi af set_, annars False.
    """
    # Breytir tuple aftur í mengi til að framkvæma samanburð á mengjum
    return all(any(sub == s for s in set_) for sub in subset)

def main():
    # Skilgreinum dæmamengi A
    A = {1, 2}
    
    # Búum til veldismengi A
    P_A = power_set(A)
    print(f"P(A): {P_A}")
    
    # Búum til veldismengi af veldismengi A
    P_P_A = power_set(P_A)
    print(f"P(P(A)): {P_P_A}")

    # Athugum hvort P(A) sé hlutmengi af P(P(A))
    subset_condition = is_subset(P_A, P_P_A)
    print(f"P(A) ⊆ P(P(A)) er {subset_condition}")

    # Prófun með fleiri dæmum
    print("\nPrófun með fleiri dæmum:")
    examples = [
        {1},           # Mengi með einu staki
        {1, 2, 3},     # Mengi með mörgum stökum
        set()          # Tómt mengi
    ]

    for example in examples:
        P_example = power_set(example)
        P_P_example = power_set(P_example)
        condition = is_subset(P_example, P_P_example)
        print(f"Mengi A: {example}, P(A): {P_example}")
        print(f"P(A) ⊆ P(P(A)) er {condition}\n")

# Keyrir aðalfallið
if __name__ == "__main__":
    main()

    # Útskýring á niðurstöðunum:
    # Fyrir mengi með eitt eða fleiri stök: P(A) ⊆ P(P(A)) er False
    # vegna þess að stök í P(A) eru ekki sett saman á sama hátt og stök í P(P(A)).
    # P(P(A)) inniheldur mengjasöfn sem samanstanda af hlutmengjum P(A), en P(A)
    # inniheldur aðeins hlutmengi A. Þess vegna eru þau ekki beint samanburðarhæf.
    #
    # Fyrir tómt mengi A: P(A) ⊆ P(P(A)) er True, því bæði P(A) og P(P(A))
    # innihalda einungis tóma mengið, og því stenst hlutmengisskilyrðið.
    #
    # Þetta sýnir að hlutmengisskilyrðið P(A) ⊆ P(P(A)) er aðeins uppfyllt þegar A er tómt mengi.