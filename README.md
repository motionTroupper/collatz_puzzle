
# Collatz Puzzle 🧩

Visual demonstration of the Collatz transformation using a finite set of seven puzzle pieces.

![Puzzle Pieces](https://github.com/motionTroupper/collatz_puzzle/blob/main/assets/puzzle_pieces.png)

<<<<<<< HEAD
---
=======
![Pieces](collatz_puzzle.png)
This project delves into the Collatz conjecture by analyzing binary representations and their transformations. It offers a unique perspective by visualizing how numbers evolve under the Collatz process, emphasizing the role of bit patterns in determining the sequence's behavior.
>>>>>>> dd0907b4027fe50b6fb22b31d77b31a129237b31

## 🧠 What is this?

This project presents a novel way to explore the Collatz conjecture through a **physical puzzle analogy**. Each puzzle piece encodes a binary bit and the propagation rules of the transformation `3n + 2^t`, where `t` is the number of trailing zeros in the binary representation of `n`.

---

## 🧩 The Puzzle

- There are **only seven distinct puzzle pieces**.
- **They cannot be rotated.**
- The **binary value** of each piece is:
  - `1` if the **bottom** of the piece has a **notch**,
  - `0` if the **bottom** is **flat**.
- The **orange piece** represents the **least significant bit (LSB)** and must always:
  - Be placed as the **rightmost piece**,
  - Be **unique** in the row.

---

## 🧱 Constructing a Number

To build a binary number using the puzzle:

1. Start from the **right**, placing the **orange piece**.
2. Add pieces to the **left**, ensuring that they fit together perfectly.
3. The number is **not complete** until the row is:
   - **Flat on the left**,
   - **Flat on the right** (only the orange piece).

---

## ⬆️ Getting the Next Collatz Number

To build the next number in the sequence:

1. Place a **new row** of puzzle pieces **above** the current one.
2. The **first `1` from the right** must again be the **orange piece**.
3. Each new piece must **fit the pieces below it**.
4. The new row is **not complete** until:
   - Every piece below is supported by a piece above,
   - The row ends **flat on both sides**.
5. The **Collatz-transformed number** is read by:
   - Reading the **bottom edges** of the new pieces,
   - From the **first to the last `1`** (no leading or trailing zero padding).

---

## ⬇️ Finding Predecessors in Collatz

To find which numbers map to the current number:

- Follow the same rules, but build **downward** instead of upward.
- **Caveat:** There may be **no solution** (e.g. for multiples of 3).
- If a solution exists, there are **infinitely many valid configurations** that lead to the upper number, or the upper number multiplied by 2^n

---

## 🔍 Underlying Hypothesis

This puzzle encodes a transformation based on:

\[
a_n = 3a_{n-1} + 	ext{gcd}(a_{n-1}, 2^{\lfloor \log_2(a_{n-1}) \rfloor})
\]

Rather than dividing by 2 when a number is even, this approach **adds back the power of two** that would have been “lost” in traditional Collatz steps.

The puzzle provides a visual way to **track and propagate carry bits**, and helps illustrate why all sequences may eventually collapse toward powers of two.

---

## 📥 Contributing

Forks and pull requests welcome! Share your own ideas, transformations, or even new visual metaphors.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).  
Created by **Raul Martinez Zabala**.
