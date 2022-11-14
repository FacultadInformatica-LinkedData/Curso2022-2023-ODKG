import React from 'react';
import styled from 'styled-components';
import { useNavigate } from 'react-router-dom';
import { useGeolocated } from "react-geolocated";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faHeartPulse, faHospital } from '@fortawesome/free-solid-svg-icons'

function Home() {
  const navigate = useNavigate()
  const { coords } = useGeolocated({ positionOptions: {enableHighAccuracy: true,}, userDecisionTimeout: 5000, });

  return (
    <Page>
      <Header>
        <h1>HealthFinder</h1>
      </Header>
      <Content>
        <div>
          <h1>What are you looking for?</h1>
        </div>
        <ButtonContrianer>
          <button onClick={() => navigate("/defibrillator")}>
            <FontAwesomeIcon icon={faHeartPulse} />
            Defibrilator
            </button>
          <button onClick={() => navigate("/hospitals")}>
            <FontAwesomeIcon icon={faHospital} />
            Hospital
          </button>
        </ButtonContrianer>
      </Content>
    </Page>
  );
}

export default Home;

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
  display: flex;
  flex-direction: column;
  justify-content: center;
`

const ButtonContrianer = styled.div`
  margin: 0 10%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-content: space-around;

  button {
    margin: 20px 0;
    background-color: #fbe7e7;
    border-radius: 8px;
    height: 5rem;
    width: 100%;
    font-size: 1.5rem;
    font-weight: bold;

    svg {
      font-size: 1.5rem;
      font-weight: bold;
      margin-right: 8px;
    }
  } 
`
