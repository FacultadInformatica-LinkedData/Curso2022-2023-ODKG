import React from 'react'
import { faPerson } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import styled from 'styled-components'

const PersonMarker = ({children, ...rest}) => {
  return (
    <StyledDiv {...rest}>
            <FontAwesomeIcon icon={faPerson} />
    </StyledDiv>
  )
}

export default PersonMarker

const StyledDiv = styled.div`

    svg {
        color: #4772fa;
        border-color: black;
        font-size: 1.5rem;
    }
`