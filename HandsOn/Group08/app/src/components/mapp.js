import React from 'react'
import GoogleMapReact from 'google-map-react';

const Mapp = ({center, origin, children}) => {
    const defaultMapProps = {
       center: {lat: 40.4167278, lng: -3.7033387}, 
       zoom: 12
    }
    
    const handleApiLoaded = (map, maps) => {
      console.log("map",map)
      console.log("maps",maps)
    }


    return (
        <div style={{ height: '45vh', width: '80vw', alignSelf: 'center' }}>
            <GoogleMapReact 
            bootstrapURLKeys={{ key: "AIzaSyBq6lLNKXRUorYEm08spBBeThMXTON0vQE" }}
            defaultCenter={defaultMapProps.center}
            center={center}
            defaultZoom={10}
            yesIWantToUseGoogleMapApiInternals
            onGoogleApiLoaded={({ map, maps }) => handleApiLoaded(map, maps)}
            >
                {children}
            </GoogleMapReact>
        </div>
    )
}

export default Mapp