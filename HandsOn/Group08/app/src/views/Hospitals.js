import React from 'react'
import Select from 'react-select';
import styled from 'styled-components'
import { useGeolocated } from "react-geolocated";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMagnifyingGlass, faArrowLeft } from '@fortawesome/free-solid-svg-icons'

import Mapp from '../components/mapp';
import PersonMarker from '../components/personMarker';
import ClinicMarker from '../components/clinicMarker';

const options = [
  { value: 'dentistry', label: 'Dentistry' },
  { value: 'Enfermería familiar y comunitaria', label: 'Enfermería familiar y comunitaria' },
];

const endpointUrl = `/sparql?query=`

const Hospitals = () => {
  const [notFound, setNotFoun] = React.useState(false)
  const [status, setStatus] = React.useState("waiting")
  const [marker, setMarker] = React.useState({lat: 0, lng: 0})
  const [selectedOption, setSelectedOption] = React.useState(null);

  const { coords } = useGeolocated({ positionOptions: {enableHighAccuracy: true,}, userDecisionTimeout: 5000, });
  const {latitude = 40.4167278, longitude = 3.7033387 } = coords ? coords : {latitude: 40.4167278, longitude: 3.7033387 }
  const center = { lat: latitude, lng: longitude }
  const minLat = center.lat - 0.1
  const maxLat = center.lat + 0.1
  const minLng = center.lng - 0.1
  const maxLng = center.lng + 0.1

  console.log(minLat)
  console.log(maxLat)
  console.log(minLng)
  console.log(maxLng)


  const clinicQuery = `PREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX%20rdfs%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX%20geo%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E%20%0APREFIX%20nsont%3A%20%3Chttps%3A%2F%2Fwww.healthfinder.io%2Fgroup08%2Fontology%2Fontology%23%3E%20%0ASELECT%20%3Fclinic%20%3Fspec%20%3Flat%20%3Flon%0A%20%20WHERE%20%7B%0A%20%20%20%20%3Fclinic%20nsont%3Aspecialization%20%22${selectedOption}%22%20.%0A%20%20%20%20%3Fclinic%20geo%3Alocation%20%3Faddress.%0A%20%20%20%20%3Faddress%20geo%3Alatitude%20%3Flat.%0A%20%20%20%20%3Faddress%20geo%3Alongitude%20%3Flon.%0A%20%20%20%20FILTER%28${minLat}%20%3C%3D%20%3Flat%20%26%26%20%3Flat%20%3C%3D%20${maxLat}%20%26%26%20${minLng}%20%3C%3D%20%3Flon%20%26%26%20%3Flon%20%3C%3D%20${maxLng}%29%0A%20%20%7D%0A%20%20LIMIT%201`

  const goSearch = () => {
    setStatus("loading")
  }


  const goBack = () => {
    setNotFoun(false)
    setStatus("waiting")
  }

  React.useEffect(() => {

    const getData = async () => {
      fetch(endpointUrl+clinicQuery, {
        headers: {"Access-Control-Allow-Origin": "*"},
        method: "GET",
      }).then((response) => response.json())
      .then((data) => {
        console.log("data", data)
        const results = data.results.bindings
        if (results.length === 0) {
          setNotFoun(true)
        } else {
          const clinic = results[0]
          const clinicCoords = { lat: parseFloat(clinic.lat.value), lng: parseFloat(clinic.lon.value)}
          setMarker(clinicCoords)
        }
        setStatus("loaded")
      })
    }

    if (status === "loading") {
      getData()
    }

  }, [status, clinicQuery])


  if (status === "loading" || !coords) {
    return (
      <Page>
        <Header>
          <h1>HealthFinder</h1>
        </Header>
        <Content>
          <h1>Loading</h1>
        </Content>
      </Page>
    )
  }

  if (notFound) {
    return (
<Page>
        <Header>
            <h1>HealthFinder</h1>
        </Header>
        <Content> 
          <h1>Result Not found</h1>
          <ButtonContainer>
            <button style={{marginTop: "10px"}} onClick={goBack}>
              <FontAwesomeIcon icon={faArrowLeft} />
              Go back
            </button>
          </ButtonContainer>
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
          {
            status === "loaded" ? 
            <>
              {/* <TextContainer>
                <p>Address:</p>
                <h1>Calle Santiago, 3</h1>
              </TextContainer> */}
              <Mapp center={center} origin={center} destination={marker}>
                {
                  marker.lat !== 0 ? 
                  <ClinicMarker text={"marker"} lat={marker.lat} lng={marker.lng} />
                  :
                  null
                }
                {
                  coords &&
                  <PersonMarker lat={latitude} lng={longitude} />
                }
              </Mapp>
              <ButtonContainer>
                <button style={{marginTop: "10px"}} onClick={goBack}>
                  <FontAwesomeIcon icon={faArrowLeft} />
                  Go back
                </button>
              </ButtonContainer>
            </>
            : 
            
              <>
              <SelectContainer>
                <h1>Select the specialization:</h1>
                <Select
                  defaultValue={selectedOption}
                  onChange={(sel) => setSelectedOption(sel.value)}
                  options={options}
                />
              </SelectContainer>
              <ButtonContainer>
                <button onClick={goSearch}>
                  <FontAwesomeIcon icon={faMagnifyingGlass} />
                  Search
                </button>
              </ButtonContainer>
            </>
            }
          
        </Content>
    </Page>
  )
}

export default Hospitals

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
  align-content: center;

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
const ButtonContainer = styled.div`
  margin: 0;
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;

  button {
    /* margin: 20px 0; */
    background-color: #fbe7e7;
    border-radius: 8px;
    height: 2.5rem;
    width: 50vw;
    font-size: 1rem;
    font-weight: bold;
    align-self: center;

    svg {
      font-size: 1.5rem;
      font-weight: bold;
      margin-right: 8px;
    }
  } 
`

const SelectContainer = styled.div`
  width: 50vw;
  align-self: center;
  margin-bottom: 1rem;
`


const TextContainer = styled.div`
  text-align: center;
  font-weight: bold;

  p, h1 {
    margin: 0;
  }

`