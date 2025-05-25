#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Session { // Дополнительный класс
private:
    string date;
    string time;
    string movieTitle;
    double ticketPrice;

public:
    // Геттеры
    string getDate() { return date; }
    string getTime() { return time; }
    string getMovieTitle() { return movieTitle; }
    double getTicketPrice() { return ticketPrice; }

    // Сеттеры
    void setDate(string d) { date = d; }
    void setTime(string t) { time = t; }
    void setMovieTitle(string mt) { movieTitle = mt; }
    void setTicketPrice(double p) { ticketPrice = p; }

    // Перегруженные методы
    void setProperties() {
        cout << "Введите дату сеанса: ";
        getline(cin, date);
        cout << "Введите время сеанса: ";
        getline(cin, time);
        cout << "Введите название фильма: ";
        getline(cin, movieTitle);
        cout << "Введите цену билета: ";
        cin >> ticketPrice;
        cin.ignore(); // Очистка буфера
    }

    void setProperties(string d, string t, string mt, double p) {
        date = d;
        time = t;
        movieTitle = mt;
        ticketPrice = p;
    }

    void displayInfo() {
        cout << "Сеанс: " << movieTitle << endl;
        cout << "Дата: " << date << ", Время: " << time << endl;
        cout << "Цена билета: " << ticketPrice << " руб." << endl;
        cout << "---------------------" << endl;
    }
};

class Cinema { // Основной класс
private:
    string name;
    string address;
    vector<Session> sessions; // Массив объектов Session

public:
    // Геттеры
    string getName() { return name; }
    string getAddress() { return address; }

    // Сеттеры
    void setName(string n) { name = n; }
    void setAddress(string a) { address = a; }

    // Метод для добавления сеанса
    void addSession(Session s) {
        sessions.push_back(s);
    }

    // Метод для отображения информации о кинотеатре
    void displayInfo() {
        cout << "Кинотеатр: " << name << endl;
        cout << "Адрес: " << address << endl << endl;
        cout << "Список сеансов:" << endl;
        cout << "=====================" << endl;
        
        for (size_t i = 0; i < sessions.size(); ++i) {
            sessions[i].displayInfo();
        }
    }
};

int main() {
    Cinema myCinema;
    
    // Установка информации о кинотеатре
    myCinema.setName("КиноМир");
    myCinema.setAddress("ул. Кинотеатральная, 15");

    // Добавление сеансов разными способами
    Session s1;
    cout << "Добавление первого сеанса (интерактивный ввод):" << endl;
    s1.setProperties();
    myCinema.addSession(s1);

    Session s2;
    cout << "\nДобавление второго сеанса (параметризованный ввод):" << endl;
    s2.setProperties("2023-12-15", "18:00", "Аватар: Путь воды", 450.0);
    myCinema.addSession(s2);

    // Вывод всей информации
    cout << "\n\nИнформация о кинотеатре:" << endl;
    cout << "=====================" << endl;
    myCinema.displayInfo();

    return 0;
}