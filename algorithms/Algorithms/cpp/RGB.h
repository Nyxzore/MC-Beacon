#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <list>
class RGB{
    public:
        double R,G,B; 

        RGB() : R(0), G(0), B(0) {}; 
        RGB(double Red, double Green, double Blue) : R(Red), G(Green), B(Blue) {};

        //display
        void print(){
            std:: cout << '(' << R << ' ' << G << ' ' << B << ')';
        }

        //operator overloading
        RGB operator+(const RGB& other) const{
            return RGB(R+other.R, G+other.G,B+other.B);
        }

        RGB operator-(const RGB& other) const{
            return RGB(R-other.R, G-other.G, B-other.B);
        }

        RGB operator*(const double& scalar)const{
            return RGB(R*scalar, G*scalar, B*scalar);
        }

        double euclid_dist(const RGB& other) const{
            return  sqrt((R-other.R)*(R-other.R)+
                     (G-other.G)*(G-other.G)+
                     (B-other.B)*(B-other.B));
        }

        bool operator<(const RGB& other) const {
        if (R != other.R) return R < other.R;
        if (G != other.G) return G < other.G;
        return B < other.B;
    }
};

static RGB beacon_colour(const std::vector<RGB>& colours){
            RGB result = colours[0]; //C_0
            size_t n = colours.size();
                for(size_t i=1; i<n; i++){
                    result = result + colours[i]*(pow(2, i-1));
                }
            return result*(1.0/(pow(2,n-1)));
        }

static RGB beacon_colour(const std::list<RGB>& colours) {
    std::vector<RGB> tmp(colours.begin(), colours.end());
    return beacon_colour(tmp); // calls the existing vector version
}



static std::map<std::string, RGB> colour_name_to_rgb = {
        {"black",       {29, 29, 33}},
        {"blue",        {60, 68, 170}},
        {"brown",       {131, 84, 50}},
        {"cyan",        {22, 156, 156}},
        {"gray",        {71, 79, 82}},
        {"green",       {94, 124, 22}},
        {"light_Blue",  {58, 179, 218}},
        {"light_Gray",  {157, 157, 151}},
        {"lime",        {1282, 199, 31}},
        {"magenta",     {199, 78, 189}},
        {"orange",      {249, 128, 29}},
        {"pink",        {243, 139, 170}},
        {"purple",      {137, 50, 184}},
        {"red",         {176, 46, 38}},
        {"white",       {249, 255, 254}},
        {"yellow",      {254, 216, 61}},
    };

static std::map<RGB, std::string> rgb_to_colour_name = {
    {{29, 29, 33},      "black"},
    {{60, 68, 170},     "blue"},
    {{131, 84, 50},     "brown"},
    {{22, 156, 156},    "cyan"},
    {{71, 79, 82},      "gray"},
    {{94, 124, 22},     "green"},
    {{58, 179, 218},    "light_Blue"},
    {{157, 157, 151},   "light_Gray"},
    {{128, 199, 31},    "lime"},
    {{199, 78, 189},    "magenta"},
    {{249, 128, 29},    "orange"},
    {{243, 139, 170},   "pink"},
    {{137, 50, 184},    "purple"},
    {{176, 46, 38},     "red"},
    {{249, 255, 254},   "white"},
    {{254, 216, 61},    "yellow"},
};
