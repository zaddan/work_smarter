#include <vector>;
#include <fstream>;
#include <boost/serialization/vector.hpp>
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <iostream>
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
      ar & randVar;    
    }
    
    
    //other junk in the class (variables)
    std::vector<std::string> filenames;
    int randVar;
public:
    void AddFilename( const std::string& filename );    
    void Print() const;
    void AddRandVar(int inputRandVar) ;
};
 
void Info::Print() const
{
    std::copy(filenames.begin(),     
              filenames.end(),     
              std::ostream_iterator<std::string>(std::cout, "\n"));     
    cout << randVar<<endl;
}
 
void Info::AddFilename( const std::string& filename )
{
    filenames.push_back( filename );    
}

void Info::AddRandVar(int inputRandVar)
{
    randVar = inputRandVar; 
}

int main(int argc, char** argv) 
{
    std::vector<Info> infos;
    Info info1, info2; 
    info1.AddFilename( "ThisFile1.txt" );
    info1.AddFilename( "ThatFile1.txt" );
    info1.AddFilename( "OtherFile1.txt" );
    info1.AddFilename( "OtherFile1.txt" );
    info1.AddRandVar(3);
    
    info2.AddFilename( "ThisFile2.txt" );
    info2.AddFilename( "ThatFile2.txt" );
    info2.AddFilename( "OtherFile2.txt" );
    info2.AddRandVar(3);
    
    infos.push_back(info1);
    infos.push_back(info2);
    
    std::ofstream ofs( "store.dat" ); //file to write to
    std::ifstream ifs( "store.dat" ); //fie to read from
    std::vector<Info> restored_infos;
    
  //store the data 
  {
      boost::archive::text_oarchive ar(ofs);
      ar <<infos;
  }    
    
  //restor the data 
  { 
        boost::archive::text_iarchive ir(ifs);
        ir >> restored_infos;
  }    

    std::vector<Info>::const_iterator it = restored_infos.begin();
    for ( ; it != restored_infos.end(); ++it )
    {
        Info info = *it;
        info.Print();
    }

  return 0;
}

