#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <memory>
#include <algorithm>
#include <cctype>

// Базовый класс для фреймов
class ID3Frame {
protected:
    std::string frameID_;
    int size_;
    std::vector<char> flags_;
    std::vector<char> data_;

public:
    ID3Frame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : frameID_(frameID), size_(size), flags_(flags), data_(data) {}
    
    virtual ~ID3Frame() = default;
    
    virtual void display() const {
        std::cout << "Frame ID: " << frameID_ << "\n";
        std::cout << "Size: " << size_ << " bytes\n";
    }
    
    const std::string& getFrameID() const { return frameID_; }
};

// Текстовые фреймы
class TextFrame : public ID3Frame {
protected:
    std::string text_;
    char encoding_;

public:
    TextFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : ID3Frame(frameID, size, flags, data) {
        parseTextData();
    }
    
    void parseTextData() {
        if (data_.empty()) return;
        
        encoding_ = data_[0];
        text_.assign(data_.begin() + 1, data_.end());
        
        // Удаление нулевых символов
        text_.erase(std::remove(text_.begin(), text_.end(), '\0'), text_.end());
    }
    
    void display() const override {
        ID3Frame::display();
        std::cout << "Text: " << text_ << "\n";
        std::cout << "Encoding: " << static_cast<int>(encoding_) << "\n";
    }
};

// Специализированные текстовые фреймы
class TitleFrame : public TextFrame {
public:
    TitleFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : TextFrame(frameID, size, flags, data) {}
    
    void display() const override {
        std::cout << "=== Title ===\n";
        TextFrame::display();
    }
};

class ArtistFrame : public TextFrame {
public:
    ArtistFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : TextFrame(frameID, size, flags, data) {}
    
    void display() const override {
        std::cout << "=== Artist ===\n";
        TextFrame::display();
    }
};

class AlbumFrame : public TextFrame {
public:
    AlbumFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : TextFrame(frameID, size, flags, data) {}
    
    void display() const override {
        std::cout << "=== Album ===\n";
        TextFrame::display();
    }
};

class YearFrame : public TextFrame {
public:
    YearFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : TextFrame(frameID, size, flags, data) {}
    
    void display() const override {
        std::cout << "=== Year ===\n";
        TextFrame::display();
    }
};

class CommentFrame : public TextFrame {
private:
    std::string language_;
    
public:
    CommentFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : TextFrame(frameID, size, flags, data) {
        parseCommentData();
    }
    
    void parseCommentData() {
        if (data_.size() < 4) return;
        
        encoding_ = data_[0];
        language_ = std::string(data_.begin() + 1, data_.begin() + 4);
        text_ = std::string(data_.begin() + 4, data_.end());
    }
    
    void display() const override {
        std::cout << "=== Comment ===\n";
        ID3Frame::display();
        std::cout << "Language: " << language_ << "\n";
        std::cout << "Text: " << text_ << "\n";
    }
};

class GenreFrame : public TextFrame {
public:
    GenreFrame(const std::string& frameID, int size, const std::vector<char>& flags, const std::vector<char>& data)
        : TextFrame(frameID, size, flags, data) {}
    
    void display() const override {
        std::cout << "=== Genre ===\n";
        TextFrame::display();
    }
};

// Фабрика фреймов
class FrameFactory {
public:
    static std::unique_ptr<ID3Frame> createFrame(const std::string& frameID, 
                                               int size, 
                                               const std::vector<char>& flags, 
                                               const std::vector<char>& data) {
        if (frameID == "TIT2") {
            return std::make_unique<TitleFrame>(frameID, size, flags, data);
        } else if (frameID == "TPE1") {
            return std::make_unique<ArtistFrame>(frameID, size, flags, data);
        } else if (frameID == "TALB") {
            return std::make_unique<AlbumFrame>(frameID, size, flags, data);
        } else if (frameID == "TYER") {
            return std::make_unique<YearFrame>(frameID, size, flags, data);
        } else if (frameID == "COMM") {
            return std::make_unique<CommentFrame>(frameID, size, flags, data);
        } else if (frameID == "TCON") {
            return std::make_unique<GenreFrame>(frameID, size, flags, data);
        } else {
            return std::make_unique<ID3Frame>(frameID, size, flags, data);
        }
    }
};

// Парсер ID3v2.4
class ID3Parser {
private:
    std::string filename_;
    std::map<std::string, std::unique_ptr<ID3Frame>> frames_;
    
    void skipUnsyncBytes(std::ifstream& file) {
        char flags;
        file.read(&flags, 1);
        if (flags & 0x80) {
            // Пропускаем unsync-байты (реализация может быть сложнее)
            std::cerr << "Warning: Unsynchronisation flag is set, proper handling required\n";
        }
    }
    
    int readSynchSafeInt(std::ifstream& file) {
        int result = 0;
        for (int i = 0; i < 4; ++i) {
            char byte;
            file.read(&byte, 1);
            result = (result << 7) | (byte & 0x7F);
        }
        return result;
    }
    
    std::string readFrameID(std::ifstream& file) {
        char id[5] = {0};
        file.read(id, 4);
        if (!isalpha(id[0])) return ""; // Проверка на валидность
        return std::string(id);
    }
    
    int readFrameSize(std::ifstream& file) {
        int size = 0;
        for (int i = 0; i < 4; ++i) {
            char byte;
            file.read(&byte, 1);
            size = (size << 8) | static_cast<unsigned char>(byte);
        }
        return size;
    }
    
    std::vector<char> readFlags(std::ifstream& file) {
        std::vector<char> flags(2);
        file.read(flags.data(), 2);
        return flags;
    }
    
    std::vector<char> readFrameData(std::ifstream& file, int size) {
        std::vector<char> data(size);
        file.read(data.data(), size);
        return data;
    }

    bool isID3v2Tag(std::ifstream& file) {
        char header[3];
        file.read(header, 3);
        if (file.gcount() != 3) return false;
        return (header[0] == 'I' && header[1] == 'D' && header[2] == '3');
    }

    bool parseFrame(std::ifstream& file) {
        // Сохраняем позицию перед чтением фрейма
        std::streampos startPos = file.tellg();
        
        std::string frameID = readFrameID(file);
        if (frameID.empty() || frameID.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") != std::string::npos) {
            file.seekg(startPos); // Возвращаем позицию
            return false;
        }

        int frameSize = readFrameSize(file);
        if (frameSize <= 0 || frameSize > 10*1024*1024) {
            file.seekg(startPos);
            return false;
        }

        auto flags = readFlags(file);
        auto data = readFrameData(file, frameSize);

        // Проверяем, что прочитали корректное количество данных
        if (data.size() != static_cast<size_t>(frameSize)) {
            file.seekg(startPos);
            return false;
        }

        frames_[frameID] = FrameFactory::createFrame(frameID, frameSize, flags, data);
        return true;
    }

public:
    ID3Parser(const std::string& filename) : filename_(filename) {}
    
    bool parse() {
        std::ifstream file(filename_, std::ios::binary);
        if (!file) {
            std::cerr << "Error opening file: " << filename_ << "\n";
            return false;
        }
        
        if (!isID3v2Tag(file)) {
            std::cerr << "No valid ID3v2 tag found\n";
            return false;
        }
        
        // Читаем версию (2 байта) и флаги (1 байт)
        char version[2];
        file.read(version, 2);
        char flags;
        file.read(&flags, 1);
        
        int tagSize = readSynchSafeInt(file);
        if (tagSize <= 0 || tagSize > 100*1024*1024) { // Максимум 100MB
            std::cerr << "Invalid tag size: " << tagSize << "\n";
            return false;
        }
        
        // Чтение фреймов
        while (file.good() && file.tellg() < 10 + tagSize) {
            if (!parseFrame(file)) {
                // Если не удалось прочитать фрейм, пропускаем 1 байт и пробуем снова
                file.seekg(1, std::ios::cur);
            }
        }
        
        return !frames_.empty();
    }
    
    void displayInfo() const {
        if (frames_.empty()) {
            std::cout << "No valid ID3 frames found in the file\n";
            return;
        }
        
        std::cout << "=== MP3 Tag Information ===\n";
        std::cout << "Number of frames found: " << frames_.size() << "\n\n";
        
        for (const auto& pair : frames_) {
            std::cout << "Frame: " << pair.first << " (" << pair.second->getFrameID() << ")\n";
            pair.second->display();
            std::cout << "-------------------------\n";
        }
    }
};

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <mp3_file>\n";
        return 1;
    }
    
    ID3Parser parser(argv[1]);
    if (parser.parse()) {
        parser.displayInfo();
    } else {
        std::cerr << "Failed to parse ID3 tags\n";
        return 1;
    }
    
    return 0;
}