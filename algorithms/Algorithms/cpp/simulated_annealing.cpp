#include "RGB.h"
#include <random>
#include <vector>
#include <cmath>

std::vector<RGB> colour_list;
std::random_device rd;
std::mt19937 gen(rd());

void SA_solver(size_t n_blocks, RGB desired_colour, double Temp, double alpha);

int main(){
    for (auto& key_value : colour_name_to_rgb) {
        colour_list.push_back(key_value.second);
    }

    SA_solver(5, RGB(32,121,32), 100, 0.01);
    return 0;
}

std::vector<RGB> get_neighbour(const std::vector<RGB>& current_perm){
    
    std::uniform_int_distribution<> rand_indx(0, current_perm.size()-1);
    std::uniform_int_distribution<> rand_colour(0, colour_list.size()-1);

    std::vector<RGB> neightbour = current_perm;
    neightbour[rand_indx(gen)] = colour_list[rand_colour(gen)];
    return neightbour;
}

std::vector<RGB> random_glass_blocks(size_t n_blocks) {
    std::vector<RGB> blocks;

    std::uniform_int_distribution<> rand_colour(0, colour_list.size() - 1);

    for (size_t i = 0; i < n_blocks; ++i) {
        blocks.push_back(colour_list[rand_colour(gen)]);
    }

    return blocks;
}

void SA_solver(size_t n_blocks, RGB desired_colour, double Temp, double alpha){

    std::uniform_real_distribution<> p_acceptance(0.0, 1.0);
    //init random guess
    std::vector<RGB> current_permutation = random_glass_blocks(n_blocks);
    RGB current_colour = beacon_colour(current_permutation);
    double current_fitness = current_colour.euclid_dist(desired_colour);

    std::vector<RGB> best_solution = current_permutation;
    RGB best_colour = current_colour;
    double best_fitness = current_fitness;

    while (Temp >=0.001){
        //get neightbour
        std::vector<RGB> neightbour = get_neighbour(current_permutation);
        RGB neightbour_colour = beacon_colour(neightbour); 
        double neightbour_fitness = neightbour_colour.euclid_dist(desired_colour);

        double delta = neightbour_fitness-current_fitness;

        if (delta < 0){
            best_solution  = neightbour;
            best_fitness = neightbour_fitness;
            best_colour = neightbour_colour;

            current_permutation  = neightbour;
            current_fitness = neightbour_fitness;
            current_colour = neightbour_colour;
        }
        else{
            double p = std::exp(-delta / Temp);
            if (p_acceptance(gen) <p){
                current_permutation  = neightbour;
                current_fitness = neightbour_fitness;
                current_colour = neightbour_colour;
            };
        }
    Temp *= alpha; 
    }

    //output
    std::cout << "Best permutation: ";
    for(RGB& colour : best_solution){
        std:: cout << rgb_to_colour_name.at(colour) << ' '; 
    }
    std:: cout << std::endl << "Best Colour: ";
    best_colour.print();
    std:: cout << std::endl << "Best Fitness: " << best_fitness << std:: endl;
}