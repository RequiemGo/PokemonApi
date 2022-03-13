#!/usr/bin/env python3.10
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Andres Castillo
# Created Date: 12/03/2022
#imports
import requests


def get_pokemons(url):
    '''the function that calls all the pokemon's names in total from pokeapi  
        and calculates conditions given to find the right names
    '''
    response = requests.get(url)
    if response.status_code != 200:
        return
    payload = response.json()
    results = payload.get('results', [])
    if not results:
        return
    counter = 0
    for pokemon in results:
        name = pokemon['name']

        if 'at' in name and name.count('a') == 2:
            counter += 1
    return counter


def procreate_raichu(urls):
    '''A function that joins URLs by egg groups selected, 
        then add all the possibles candidates for procreating with Raichu 
        and finally with set remove duplicates
    '''
    lovers = []
    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            continue
        payload = response.json()
        pokemon_species = payload.get('pokemon_species', [])
        if not pokemon_species:
            continue
        for pokemon in pokemon_species:
            name = pokemon['name']
            lovers.append(name)
    remove_repeated = set(lovers)
    final_lovers = list(remove_repeated)
    return len(final_lovers)


def pokemons_weight(url_fighting):
    '''In this function load URL fighting and then get into key pokemon, 
        then access its URL with an iteration to find and identify the IDs so gets weight 
        at the same time and finally does the operation with the conditions given it
    '''
    pokemons_weight1 = []
    response = requests.get(url_fighting)
    if response.status_code != 200:
        return
    payload = response.json()
    pokemon = payload.get('pokemon', [])
    if not pokemon:
        return
    urls_pokemons_fighting = [types['pokemon']['url'] for types in pokemon]
    for pokemons in urls_pokemons_fighting:
        response = requests.get(pokemons)
        if response.status_code != 200:
            continue
        payload = response.json()
        id = payload.get('id', [])
        if id > 151:
            continue
        weight = payload.get('weight', [])
        if not weight:
            continue
        pokemons_weight1.append(weight)
    return [max(pokemons_weight1), min(pokemons_weight1)]


if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/?offset=0&limit=1295'
    url_field_group = 'https://pokeapi.co/api/v2/egg-group/ground/'
    url_fairy_group = 'https://pokeapi.co/api/v2/egg-group/fairy/'
    urls = [url_field_group, url_fairy_group]
    url_fighting = 'https://pokeapi.co/api/v2/type/fighting/'
    print('Total names: ' + str(get_pokemons(url)))
    print('Total lovers <3 : ' + str(procreate_raichu(urls)))
    print('Maximum and minimum weight: ' + str(pokemons_weight(url_fighting)))
