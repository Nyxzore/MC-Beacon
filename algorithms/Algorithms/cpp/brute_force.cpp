#include "RGB.h"
#include "odometer.h"

int main() {

    //Input
    int n_desired_glass_blocks;
    std:: cout << "Enter num desired blocks: ";
    std:: cin >> n_desired_glass_blocks;

    std:: cout << "Enter num desired colour(i.e 32 121 76): ";
    double R,G,B;
    std:: cin >>R>>G>>B;
    RGB desired_colour(R,G,B);

    //tracker for best
    double best_fitness = 9999;
    RGB best_colour;
    std::vector<RGB> best_glass_block_perm;
    //Compute all perms and fitness
    Odometer permutations(n_desired_glass_blocks, colour_list.size());
    do{
        //compute
        std::vector<RGB> glass_block_perm;
        for (int& digit : permutations.get_digits()){
            glass_block_perm.push_back(colour_list[digit]);
        }
        
        //fitness
        RGB colour = beacon_colour(glass_block_perm);
        double fitness = colour.euclid_dist(desired_colour);
        if (fitness < best_fitness){
            best_fitness = fitness; 
            best_colour = colour; 
            best_glass_block_perm = glass_block_perm; 
        }
    } while (permutations.increment());
    
    //output
    std::cout << "Best permutation: ";
    for(RGB& colour : best_glass_block_perm){
        std:: cout << rgb_to_colour_name.at(colour) << ' '; 
    }
    std:: cout << std::endl << "Best Colour: ";
    best_colour.print();
    std:: cout << std::endl << "Best Fitness: " << best_fitness << std:: endl;
    return 0;
}