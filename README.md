# Projekt_Selenium_sklep_Pinokio

## Opisy przypadków testowych

  # Scenariusz testowy:
Złożenie zamówienia w ilości przekraczającej maksymalną liczbę dla jednego rodzaju produktu oraz złożenie zamówienia przez użytkownika wybierającego kraj dostawy inny niż Polska. 

  # Przypadki testowe:
  
001: Złożenie zamówienia w ilości przekraczającej maksymalną możliwą do zakupu liczbę produktów jednego rodzaju.

002: Zakup produktów przez użytkownika wybierającego dostawę poza Polskę.

  # Środowisko: 
Chrome wersja 100.0.4896.60, Windows 10 Home 21H2

  # Warunki wstępne:
1.	Otwarta strona główna: https://pinokio.pl.
2.	Użytkownik niezalogowany.

  # Kroki dla przypadku testowego 001:
1.	Kliknij "Dziewczynka".
2.	Wybierz produkt "Spódnica jeans Romantic".
3.	Wybierz rozmiar produktu.
4.	Wpisz żądaną liczbę produktów powyżej 9999.
5.	Zatwierdź produkty w koszyku.
6.	Sprawdź, czy pojawia się informacja o dodaniu produktu do koszyka.
7.	Przejdź do koszyka.
8.	Sprawdź, czy pojawia się informacja o braku możliwości zamówienia więcej niż 9999 sztuk jednego produktu oraz o zmniejszeniu ilości produktów w koszyku.
9.	Sprawdź, czy faktyczna liczba produktów w Twoim Koszyku została zmniejszona do 9999 sztuk.

  # Kroki dla przypadku testowego 002:
1.	Kliknij "Dziewczynka".
2.	Wybierz produkt "Spódnica jeans Romantic".
3.	Wybierz rozmiar produktu.
4.	Wpisz żądaną liczbę produktów.
5.	Zatwierdź produkty w koszyku.
6.	Sprawdź, czy pojawia się informacja o dodaniu produktu do koszyka.
7.	Przejdź do koszyka.
8.	Wybierz kraj dostawy inny niż Polska.
9.	Kliknij "Zamawiam".
10.	Sprawdź, czy pojawia się komunikat o błędach.
        
  # Oczekiwany rezultat:
- dla przypadku testowego 001:
1.	Użytkownik otrzymuje komunikat: „Uwaga! Nie można zamówień więcej niż 9999 sztuk jednego produktu. Produktowi Spódnica jeans Romantic została zmniejszona ilość w koszyku.”
2.	Przy wpisaniu większej ilości niż 9999, ilość w koszyku automatycznie zmniejsza się do 9999 szt. wybranego produktu - brak możliwości zakupu więcej niż 9999 sztuk jednego produktu.
- dla przypadku testowego 002:
1.	Użytkownik otrzymuje komunikat: 
„W Twoim koszyku znajdują się następujące błędy:
Nie wybrano punktu płatności.
Nie można wybrać wybranej formy płatności.
Nie można wybrać wybranej formy dostawy.”
2.	Produkty nie zostały zakupione.

## Kod



## Uwagi końcowe

Automatyzacja przypadków testowych powiodła się. Test może być wrażliwy na zmianę struktury strony z powodu użycia lokalizatorów XPATH, które odnoszą się do kolejności elementów na stronie oraz z powodu zmian zachodzących na stronie.

