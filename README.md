# Ohjelmistotekniikka, harjoitustyö (StrengthApp)

Sovelluksen avulla käyttäjät pystyvät seuraamaan voimailulajien suorituksiaan.

## Dokumentaatio
- [Vaatimusmäärittely](/python-strength-app/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](/python-strength-app/dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](/python-strength-app/dokumentaatio/changelog.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```



