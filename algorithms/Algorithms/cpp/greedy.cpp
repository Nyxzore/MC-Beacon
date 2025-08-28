#include "RGB.h"

struct beacon{
    RGB colour;
    std::vector<RGB> glass_block_permutation; 
    double fitness;
};

int main(){
    //avail colour list
    std::vector<RGB> colour_list;
    for (auto& key_value : colour_name_to_rgb) {
        colour_list.push_back(key_value.second);
    }

    //input
    int n_desired_glass_blocks;
    std:: cout << "Enter num desired blocks: ";
    std:: cin >> n_desired_glass_blocks;

    std:: cout << "Enter num desired colour(i.e 32 121 76): ";
    double R,G,B;
    std:: cin >>R>>G>>B;
    RGB desired_colour(R,G,B);

    beam_width = 16; 
    //greedy
    std::vector<RGB> best_glass_block_perm; 

    vector<beacon> candidates;
    candidates.push_back(beacon());

    
    //output
    std::cout << "Best permutation: ";
    for(RGB& colour : best_glass_block_perm){
        std:: cout << rgb_to_colour_name.at(colour) << ' '; 
    }
    RGB final_colour = beacon_colour(best_glass_block_perm);
    double final_fitness = final_colour.euclid_dist(desired_colour);
    std:: cout << std::endl << "Best Colour: ";
    final_colour.print();
    std:: cout << std::endl << "Best Fitness: " << final_fitness << std:: endl;
    return 0;
}