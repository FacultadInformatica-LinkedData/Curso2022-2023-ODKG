import React from 'react'
import { faHeartPulse } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import styled from 'styled-components'

const Marker = ({children, ...rest}) => {
  return (
    <StyledDiv {...rest}>
            <FontAwesomeIcon icon={faHeartPulse} />
    </StyledDiv>
  )
}

export default Marker

const StyledDiv = styled.div`

    svg {
        color: red;
        font-size: 1.5rem;

    }
`