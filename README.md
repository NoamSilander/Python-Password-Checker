# Password Strength Checker
A simple password strength checker I built in Python.

Works by comparing each character of your password in a `for` loop to a different condition (e.g. lowercase, uppercase). If it finds one, (e.g. an uppercase letter), it gives you one point. The amount of points correspond to a strength rating.

The script asks you for a string (your password), then it runs it through many checkers and prints the result of each checker. At the end, the script tells you what to improve in the password.

The strength rating goes as follows:

`1`: `Very weak`

`2`: `Weak`

`3`: `Average`

`4`: `Strong`

`5`: `Very strong (good job)`


## How to Run
1. Run `PasswordChecker.py`

## Example
1. Password is `michael123`

```
Enter a password (enter to exit): michael123
Length: 10 characters
Lowercase: yes
Uppercase: no
Number: yes
Symbol: no
Strength: Weak
To improve: Make it atleast 12 characters, Add uppercase letters, Add symbols
```

2. Password is `MichaelBanana123#`

```
Enter a password (enter to exit): MichaelBanana123#
Length: 17 characters
Lowercase: yes
Uppercase: yes
Number: yes
Symbol: yes
Strength: Very strong (good job)
To improve: None
```