#include <iostream>

int count_digits(int number) {
    int ans = 0;
    long long ten_pw = 1;
    while (number / ten_pw != 0) {
        ten_pw *= 10;
        ++ans;
    }
    return ans;
}
bool is_ascending(int number) {
    const int num_digits = count_digits(number);
    int div_by = 10;
    int prev_dig = 11;
    for (int i = 0; i < num_digits; i++) {
        int next_dig = number % div_by;
        next_dig /= (div_by/10);
        if (next_dig >= prev_dig) {
            return false;
        }
        prev_dig = next_dig;
        div_by*=10;
    }
    return true;
}
// this simulation excludes 9 digit numbers because they literally take more than a minute on my computer
int main() {
    size_t mult = 1;
    for (int _ = 0; _ < 9; ++_) {
        if (_ == 0) {
            mult = 0;
        } else if (_ == 1) {
            mult = 1;
        }
        size_t count = 0;
        
        for (int number = mult; number <= mult*10; ++number) {
            count += is_ascending(number);
        }
        
        std::cout << count_digits(mult) << " digits: " << count << '\n';
        mult *= 10;
    }
}
