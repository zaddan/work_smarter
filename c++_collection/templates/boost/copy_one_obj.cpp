#include <vector>;
#include <fstream>;
#include <boost/serialization/vector.hpp>
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
using namespace std; 

//some class info
class Info
{
private:
    // Allow serialization to access non-public data members.
    //both of the followings are necessary to be defined in the desired class 
    friend class boost::serialization::access;
      
    // Serialize the std::vector member of Info
    template<class Archive>
    void serialize(Archive & ar, const unsigned int version)
    {
      ar & filenames;    
    }
    
    
    //other junk in the class (variables)
    std::vector<std::string> filenames;

public:
    void AddFilename( const std::string& filename );    
    void Print() const;

};
 
void Info::Print() const
{
    std::copy(filenames.begin(),     
              filenames.end(),     
              std::ostream_iterator<std::string>(std::cout, "\n"));     
}
 
void Info::AddFilename( const std::string& filename )
{
    filenames.push_back( filename );    
}
 
int main(int argc, char** argv) 
{
    Info *info = new Info();
    info->AddFilename( "ThisFile.txt" );
    info->AddFilename( "ThatFile.txt" );
    info->AddFilename( "OtherFile.txt" );
    std::ofstream ofs( "store.dat" ); //file to write to
    std::ifstream ifs( "store.dat" ); //fie to read from
    Info *restored_info;

  //store the data 
  {
      boost::archive::text_oarchive ar(ofs);
      ar <<info;
  }    
    
  //restor the data 
  { 
        boost::archive::text_iarchive ir(ifs);
        ir >> (restored_info);
  }    
  
  restored_info->Print();
  return 0;
}

