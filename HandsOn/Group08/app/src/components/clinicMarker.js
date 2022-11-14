import React from 'react'
import { faHospital } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import styled from 'styled-components'

const ClinicMarker = ({children, ...rest}) => {
  return (
    <StyledDiv {...rest}>
            <FontAwesomeIcon icon={faHospital} />
    </StyledDiv>
  )
}

export default ClinicMarker

const StyledDiv = styled.div`

    svg {
        color: black;
        font-size: 1.5rem;
    }
`