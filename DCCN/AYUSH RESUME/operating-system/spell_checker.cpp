#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <cctype>

using namespace std;

unordered_set<string> dictionary;

// Clean word by removing punctuation and converting to lowercase
string cleanWord(const string& word) {
    string cleaned;
    for (char c : word) {
        if (isalpha(c)) {
            cleaned += tolower(c);
        }
    }
    return cleaned;
}

void loadDictionary(const string& dictFile) {
    ifstream file(dictFile);
    string word;
    while (file >> word) {
        string cleaned = cleanWord(word);
        if (!cleaned.empty()) {
            dictionary.insert(cleaned);
        }
    }
}

void checkSpelling(const string& inputFile) {
    ifstream file(inputFile);
    string line;
    int lineNum = 1;
    
    while (getline(file, line)) {
        istringstream iss(line);
        string word;
        
        while (iss >> word) {
            string cleaned = cleanWord(word);
            if (!cleaned.empty() && !dictionary.count(cleaned)) {
                cout << "Line " << lineNum << ": '" << word << "'\n";
            }
        }
        lineNum++;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        cerr << "Usage: " << argv[0] << " <dictionary> <input>\n";
        return 1;
    }

    loadDictionary(argv[1]);
    checkSpelling(argv[2]);

    return 0;
}