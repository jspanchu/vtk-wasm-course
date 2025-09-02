#include <cstdlib>
#include <iostream>

int main(int, char *[]) {
  // Get the GREETING variable from the environment
  const char *greeting = std::getenv("GREETING");
  if (greeting) {
    std::cout << greeting << '!' << std::endl;
  } else {
    std::cout << "GREETING not set!" << std::endl;
  }
  return 0;
}
