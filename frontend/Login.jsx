import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { toast } from 'react-toastify'

const Login = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      // Dummy login
      if (email === 'ogrenci@example.com') {
        toast.success("Öğrenci girişi başarılı")
        navigate('/dashboard')
      } else if (email === 'ogretmen@example.com') {
        toast.success("Öğretmen girişi başarılı")
        navigate('/dashboard')
      } else {
        toast.error("Geçersiz giriş")
      }
    } catch (err) {
      toast.error("Giriş hatası")
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{ padding: '20px' }}>
      <h2>Giriş Yap</h2>
      <input
        type="email"
        placeholder="E-posta"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      /><br />
      <input
        type="password"
        placeholder="Şifre"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      /><br />
      <button type="submit">Giriş</button>
    </form>
  )
}

export default Login