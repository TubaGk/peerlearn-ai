import React from 'react'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <nav style={{ padding: '10px', background: '#333', color: '#fff' }}>
      <Link to="/" style={{ color: '#fff', marginRight: '20px' }}>Anasayfa</Link>
      <Link to="/login" style={{ color: '#fff', marginRight: '20px' }}>Giriş</Link>
      <Link to="/dashboard" style={{ color: '#fff' }}>Panel</Link>
    </nav>
  )
}

export default Navbar