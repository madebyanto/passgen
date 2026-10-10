# Passgen

I was bored, so I made this tiny tool to generate totally local passwords for whatever I need
No cloud, no weird online service, no tracking. Just a simple random password made right on your machine

## how 2 use it

```bash
passgen 16
```

That gives u a password with 16 chars.

Want another size?

```bash
passgen 32
```

## install it globally

From the project folder:

```bash
./install.sh
```

Then u can just run:

```bash
passgen 20
```

## help

If u wanna see the options, just ask the tool:

```bash
passgen --help
```

It shows the default length, the syntax, and extra flags u can use

## notes

- the password is random
- it includes lowercase, uppercase, numbers, and symbols
- it is meant for local use only

If u want a stronger password, just bump the length

# GPL

If u wanna fork the project, go ahead
If u make changes and wanna send a pull request, also go ahead
This project is open 4 remixing, improving, and sharing