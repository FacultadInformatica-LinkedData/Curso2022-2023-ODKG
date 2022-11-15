import React from 'react'

import Home from '../views/Home'
import Hospitals from '../views/Hospitals'
import Defibrilator from '../views/Defibrilator'

const routes = [
    {
        path: '/',
        element: <Home />
    },
    {
        path: '/hospitals',
        element: <Hospitals />
    },
    {
        path: '/defibrillator',
        element: <Defibrilator />
    }
]

export default routes