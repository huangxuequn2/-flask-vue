import requests from './requsts'

export const reqPing = () => requests.get(`/ping`)