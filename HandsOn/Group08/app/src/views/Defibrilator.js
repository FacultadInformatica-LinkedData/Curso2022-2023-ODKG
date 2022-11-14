import React from 'react'
import styled from 'styled-components'
import { useGeolocated } from "react-geolocated";

import Mapp from '../components/mapp';
import Marker from '../components/marker';
import PersonMarker from '../components/personMarker';
import ClinicMarker from '../components/clinicMarker';

const endpointUrl = `/sparql?query=`

window.Buffer = window.Buffer || require("buffer").Buffer;

const Defibrilator = () => {
    const { coords } = useGeolocated({ positionOptions: {enableHighAccuracy: true,}, userDecisionTimeout: 5000, });
    const [loading, setLoading] = React.useState(true)
    const [marker, setMarker] = React.useState({lat: 0, lng: 0})
    const [marker2, setMarker2] = React.useState({lat: 0, lng: 0})
    console.log(coords)

    const {latitude = 40.4167278, longitude = 3.7033387 } = coords ? coords : {latitude: 40.4167278, longitude: 3.7033387 }
    const center = { lat: latitude, lng: longitude }
    const minLat = center.lat - 0.05
    const maxLat = center.lat + 0.05
    const minLng = center.lng - 0.05
    const maxLng = center.lng + 0.05
    
    const defibQuery = `PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20geo%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E%20%0A%0ASELECT%20%3Fdefibrillator%20%3Flat%20%3Flon%0A%20%20WHERE%20%7B%0A%20%20%20%20%3Fdefibrillator%20geo%3Alocation%20%3Faddress.%0A%20%20%20%20%3Faddress%20geo%3Alatitude%20%3Flat.%0A%20%20%20%20%3Faddress%20geo%3Alongitude%20%3Flon.%0A%20%20%20%20FILTER%28${minLat}%20%3C%3D%20%3Flat%20%26%26%20%3Flat%20%3C%3D%20${maxLat}%20%26%26%20${minLng}%3C%3D%20%3Flon%20%26%26%20%3Flon%20%3C%3D%20${maxLng}%29%0A%20%7DLIMIT%201`

    const clinicQuery = `PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20geo%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E%20%0APREFIX%20nsont%3A%20%3Chttps%3A%2F%2Fwww.healthfinder.io%2Fgroup08%2Fontology%2Fontology%23%3E%20%0ASELECT%20%3Fclinic%20%3Fspec%20%3Flat%20%3Flon%0A%20%20WHERE%20%7B%0A%20%20%20%20%3Fclinic%20nsont%3Aspecialization%20%3Fspec.%0A%20%20%20%20%3Fclinic%20geo%3Alocation%20%3Faddress.%0A%20%20%20%20%3Faddress%20geo%3Alatitude%20%3Flat.%0A%20%20%20%20%3Faddress%20geo%3Alongitude%20%3Flon.%0A%20%20%20%20FILTER%28${minLat-0.1}%20%3C%3D%20%3Flat%20%26%26%20%3Flat%20%3C%3D%20${maxLat+0.1}%20%26%26%20${minLng-0.1}%20%3C%3D%20%3Flon%20%26%26%20%3Flon%20%3C%3D%20${maxLng+0.1}%29%0A%20%20%7D%0A%20%20LIMIT%201`


    React.useEffect(() => {
        // const getData = fetch(endpointUrl)
        const getData = async () => {
          fetch(endpointUrl+defibQuery, {
            headers: {"Access-Control-Allow-Origin": "*"},
            method: "GET",
          }).then((response) => response.json())
          .then((data) => {
            const defib = data.results.bindings[0] 
            const defibCoords = { lat: parseFloat(defib.lat.value), lng: parseFloat(defib.lon.value)}
            console.log(data.results.bindings)
            console.log(defibCoords)
            setMarker(defibCoords)
            setLoading(false)
          })
          fetch(endpointUrl+clinicQuery, {
            headers: {"Access-Control-Allow-Origin": "*"},
            method: "GET"
          }).then((response) => response.json())
          .then((data) => {
            const clinic = data.results.bindings[0] 
            const clinicCoords = { lat: parseFloat(clinic.lat.value), lng: parseFloat(clinic.lon.value)}
            console.log("clinic result", data.results.bindings)
            console.log("clinic coords", clinicCoords)
            setMarker2(clinicCoords)
            setLoading(false)
          })
        }
        getData()
    }, [defibQuery, clinicQuery])


    if (loading || !coords) {
      return(
        <Page>
          <Header><h1>HealthFinder</h1></Header>
          <Content>
            <p>Loading...</p>
          </Content>
        </Page>

      )
    }

    return (
      <Page>
        <Header>
            <h1>HealthFinder</h1>
        </Header>
        <Content>
          {/* <TextContainer>
            <p>Address:</p>
            <h1>Calle Santiago, 3</h1>
          </TextContainer> */}
          <Mapp center={center}>
            {
              marker.lat !== 0 ? 
              <Marker text={"marker"} lat={marker.lat} lng={marker.lng} />
              :
              null
            }
            {
              marker2.lat !== 0 ? 
              <ClinicMarker text={"marker"} lat={marker2.lat} lng={marker2.lng} />
              :
              null
            }
            {
              coords &&
              <PersonMarker lat={latitude} lng={longitude} />
            }
          </Mapp>
        </Content>
      </Page>
    )
}

export default Defibrilator

const Page = styled.div`
  height: 100vh;
  width: 100vw;
`
const Header = styled.div`
  width: 100vw;
  border-radius: 0 0 10% 10%;
  background-color: #8a3c3c;
  height: 10vh;
  display: flex;
  justify-content: center;
  align-items: center;

  h1 {
    color: white;
    font-family: 'Bungee Shade', cursive;
    font-weight: bolder;
  }
`

const Content = styled.div`
  text-align: center;
  height: 90vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
`

const TextContainer = styled.div`
  text-align: center;
  font-weight: bold;

  p, h1 {
    margin: 0;
  }

`