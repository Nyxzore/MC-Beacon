#include "RGB.h"
#include <algorithm>
#include <list>

struct BeaconBeam{
    RGB colour;
    std::list<RGB> glass_block_permutation; 
    double fitness;
    
    static bool better(const BeaconBeam& a, const BeaconBeam& b){
        return a.fitness < b.fitness; 
    }
};

int main(){
    //avail colour list
    std::vector<RGB> colour_list;
    for (auto& key_value : colour_name_to_rgb) {
        colour_list.push_back(key_value.second);
    }

    //input
    int n_desired_glass_blocks;
    std:: cout << "Enter num desired blocks: " << std::endl;
    std:: cin >> n_desired_glass_blocks;

    std:: cout << "Enter num desired colour(i.e 32 121 76): " << std::endl;
    double R,G,B;
    std:: cin >>R>>G>>B;
    RGB desired_colour(R,G,B);

    size_t beam_width;
    std::cout << "Enter number of saved solutions at each step(beam width): " << std::endl;
    std::cin >> beam_width;  

    //greedy
    std::vector<BeaconBeam> candidates;
    candidates.push_back(BeaconBeam{ RGB(), {}, 0.0 });

    for(size_t n=0; n<n_desired_glass_blocks; n++){
        std::vector<BeaconBeam> new_candidates;
        for(BeaconBeam& beacon_beam:candidates){
            for(const RGB& colour : colour_list){
                beacon_beam.glass_block_permutation.push_front(colour);
                    beacon_beam.colour = beacon_colour(beacon_beam.glass_block_permutation);
                    beacon_beam.fitness = beacon_beam.colour.euclid_dist(desired_colour);
                    new_candidates.push_back(beacon_beam);
                beacon_beam.glass_block_permutation.pop_front();
            }
        } 

        //prune
        std:: sort(new_candidates.begin(), new_candidates.end(), BeaconBeam::better);

        candidates.clear();
        for(size_t i=0; i<std::min(beam_width, new_candidates.size()); i++){
            candidates.push_back(new_candidates[i]); 
        }

    }
    
    //output

    if (candidates.empty()) {
    std::cout << "No candidates generated.\n";
    return 0;
    }

    BeaconBeam best = candidates.front();
    RGB final_colour = best.colour;
    double final_fitness = best.fitness;


    std::cout << "Best permutation: ";
    for(RGB& colour : best.glass_block_permutation){
        std::cout << rgb_to_colour_name.at(colour) << ' '; 
    }

    std:: cout << std::endl << "Best Colour: ";
    final_colour.print();
    std:: cout << std::endl << "Best Fitness: " << final_fitness << std:: endl;
    return 0;
}