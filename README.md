Autor: Mateusz Zalewski

Cel:
Napisać program grający w rewersi. Powinna być możliwość rozgrywki na planszy o wybranym
na początku gry rozmiarze planszy (nie musi być kwadratowa) gdzie wysokość i szerokość jest z
zakresu od 8 do 30
Powinna być możliwość gry:
dwóch osób ze sobą,
osoby z komputerem,
komputera z komputerem.
Program powinien kontrolować poprawność wykonywanych ruchów. Interfejs z użytkownikiem
może być tekstowy.
Bardzo istotną częścią zadania jest opracowanie i zaimplementowanie jak najlepszego
algorytmu grającego w grę:
Modut realizujący algorytm gry komputera musi być wydzielony.

Klasy:
BoardSize - Klasa ta odpowiada za wyświetlanie okna wyboru wielkości planszy, odpowiada także
za zczytywanie informacji z okienek w których użytkownik wpisuje na jakiej planszy chciałby grać.

InputBox - Jest to klasa tworząca okienka w które użytkownik może wpisać wartość która jest w nich wyświetlana.
Można ustawić zakres wartości jaki chcemy aby był dozwolony do wpisania, w przypadku wpisania wartości niepoprawnej
okienko podświetli się na czerwono.

Board - Klasa ta odpowiada za logikę samej gry, są tu metody sprawdzające poprawność ruchu oraz wykonujące go.
Jest tu też metoda sprawdzająca czy gra się zakończyła.

Computer - W tej klasie zawarty jest algorytm grający w grę

Engine - W tej klasie znajduje się główna pętla w której znajduje się gra. Jest to klasa wywoływana przy odpaleniu gry.

Game - Klasa ta odpowiada za wyświetlanie gry, zbiera także informacje w którą komórkę kliknął gracz oraz zapewnia turowość gry.

Menu - Klasa to odpowiada za wyświetlanie menu i tworzenie przycisków wyboru trybu

Player - Wykonuje ruch gracza

Window - Inicjalizuje okno oraz wyświetla obraz w tle. Zwraca aktualne wymiary okna jako, że gra jest dostosowana do grania na różnej wielkości okienkach

Instrukcja:
Należy uruchomić program z pliku "main". Należy jednak mieć zainstalowaną bibliotekę pygame oraz os.

Podsumowanie:
Zrobienie gry było większym wyzwaniem niż mi się z początku wydawało. Największym wyzwaniem była pętla gry i decyzje jakie metody w niej wywoływać
i co się w tych metodach powinno znajdować. Pierwszym wyzwaniem jednak było nauczenie się jak działają klasy, bo jednak użycie było zupełnie inne niż na zajęciach.
Jeśli chodzi o rzeczy których nie udało się wykonać to przerw pomiędzy ruchami gracz-komputer, komputer-komputer, żeby nie było to natychmiastowe,
ale przy próbie wprowadzenia opóźnienia program z przyczyn mi nie znanych zaczyna wariować i dziwnie działać, powodując nawet taki błąd jak niemożliwość
zamknięcia okna.