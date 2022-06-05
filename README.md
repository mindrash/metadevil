# metadevil.io
Discovering interesting utility, patterns, and representations of metadata.

## hexadomain
[Polyscan](https://polygonscan.com/address/0x752cd43b36171a5c49fdbdf74574c6edff439e81) | 
[Discord](https://discord.gg/HWnrVSBC) | 
[Twitter](https://twitter.com/mindrash) | 
[Rarible](https://rarible.com/metadevil-io/items) | 
[PEBKAC.fyi](https://pebkac.fyi) | 
[itsmookie.com](https://itsmookie.com)

This project is a combination of the mining of metadata combined with automated visualization. Each piece is contrived from only a vague understanding of a randomly chosen domain name and influenced by the metadata of that glimpse. It’s like looking at a beautiful creek to paint a picture or conversely the rotting corpse of roadkill. It is wonderful to see the beauty or weirdness of one next to the stoicism of another knowing what inspired it underneath. The name of each piece is the domain base64 encoded - you can decode if you are so inclined.

- Will some pieces influenced by certain domains seem more worthwhile?
- Will categories of domains be more appreciated while and others are shunned?
- Does the viewer even care much about the domain?
- Does the art superceded the domain?
- Which seem more endearing than others? 
    - Comparitive rarity or uniqueness in the total set 
    - General element rarity
    - Color palette
    - Layout

It was decided to base64 encode the domain as the title of each piece. You can decode if you are so inclined or directly view on the nft attributes.

Contract: 0x752cd43b36171a5c49fdbdf74574c6edff439e81

## listed on
- [Rarible](https://rarible.com/metadevil-io/items)
- [Element](https://www.element.market/collections/metadevil-io)
- [tofuNFT](https://tofunft.com/nft/polygon/0x752CD43b36171A5C49fdBDF74574C6EdfF439e81/7)

## examples 
See below for some walk throughs on my thoughts on why some rendered the way they did

![metadevil](./docs/examples.png)

## the process
From a superset of dot com domain names, metadevil randomly parsed out 49,991 apex domains (also incuding www) that returned a 200 - 400 HTTP status code in the response. Hopefully there is good international variety across the set. Next, metadevil retrieved a glipse of 17,286 of these domains limited by the request timeout (metadevil doesn't have all day). With each glipse metadevil modifies the image layering in elements and other attributes influenced by the metadata of the glipse and from the HTTP response content including total number of cookies and total bytes recieved. See the attribute table below for more information about how the elements are influenced by the domain and their randomness.

### select domains
Selecting the domains took ~8 hours and 26 minutes to randomly find 49,991 domains for the base set. There will be error conditions in producing the final 10,000, so we need a larger amount to account for these.

While each was checked for a HTTP response, that does not mean there is neccessarily a "healthy" web site on the other end. Some will be parked, others my no longer be available given whatever point in time we choose. They all still produce interesting results and especially as a total collection. There is no manual review to interveen in this process selection performed by metadevil.
```
root - INFO - ********************************************************************************
root - INFO - Starting: 2022-04-25 07:53:03.846878
root - WARNING - ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
root - INFO - 3:www.serviceestufasorbis.com
...
root - INFO - 49991:www.haxyx.com
root - INFO - ********************************************************************************
root - INFO - Finished: 2022-04-25 14:29:31.595396
```

### get domain glipse
glipses took ~12 hours and 33 minutes
```
root - INFO - ********************************************************************************
root - INFO - Starting: 2022-04-25 15:35:37.184921
root - INFO - Getting url: http://www.serviceestufasorbis.com
root - INFO - Source length: 5540
root - INFO - Cookies: 0
root - INFO - Saving image: d3d3LnNlcnZpY2Vlc3R1ZmFzb3JiaXMuY29t.png
root - INFO - ['www.serviceestufasorbis.com', '5540', '0']
...
root - INFO - ********************************************************************************
root - INFO - Finished: 2022-04-26 03:58:24.452855
```

### create metadevil hexadomain
The pieces generate at about 8/min taking over 22 hours to generate 10,000 final metadevil hexadomains.
```
root - INFO - ********************************************************************************
root - INFO - Starting: 2022-04-26 09:28:35.330703
root - INFO - data_elements[]: /projects/metadevil/metadevil-glimpse/d3d3LnZhbGRlem11bm96bGFuZHNjYXBpbmcuY29t.csv
root - INFO - Processed: 1
...

```
I spoke too soon ... there were many that could not produce because of "blank" views with not enough pixel data. Two batches came together to form the final 10,000. In all I believe this took about 36 hours... 

## attributes

| attribute_name       | description                                                               |
|----------------------|---------------------------------------------------------------------------|
| domain               | 49,991 apex domains randomly selected from the superset of domains |
| cookies              | The number of cookies found on the HTTP response. Influences number of chars and if > 10 adds extra line |
| response_total_bytes | The total bytes of the response. Influences line number and width         |
| lines                | line count influence and width influenced by bytes. color influenced by palette
| ellipse_count        | 5 total possible. likelihood of 4: 10% 5: 1% |
| freak_ellipse_count  | 33% chance (a grid of colored circles randomly influenced by palette). color influenced by palette |
| chars_number         | a unicode unknown char influenced by cookie count |

Example meta.json generated
```json
{
    "name": "d3d3LnBheXRlem9zLmNvbQ==",
    "description": "Influenced by a random domain name using the site's layout, color palette, and metadata including cookie count and total response bytes.",
    "image": "[[IPS_URL]]",
    "attributes": [
        {
            "trait_type": "domain",
            "value": "www.paytezos.com"
        },
        {
            "trait_type": "cookies",
            "value": "1"
        },
        {
            "trait_type": "response_total_bytes",
            "value": 32457
        },
        {
            "trait_type": "line_number",
            "value": 3
        },
        {
            "trait_type": "ellipse_count",
            "value": 2
        },
        {
            "trait_type": "freak_ellipse_count",
            "value": 0
        },
        {
            "trait_type": "chars_number",
            "value": 0
        },
        {
            "trait_type": "created_by",
            "value": "mindrash"
        },
        {
            "trait_type": "collection",
            "value": "metadevil"
        },
        {
            "trait_type": "collection_type",
            "value": "hexadomain"
        },
        {
            "trait_type": "non-affiliation disclaimer",
            "value": "We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with the the domain. The name in use, as well as related names, marks, emblems, and images are registered trademarks of their respective owners."
        }
    ]
}
```

## technologies 
- Python - for instance creation including metadata and image rendering
- IPFS - for this project off chain is best. These were pinned with Pinata.
- Alchemy - chain api
- Hardhat - wrestled with truffle and brownie on some things and hardhat won
- Node - for contract and minting
- Polygon - wanted to go side chain for cost considerations, but not sold that this was the best idea
- Solidity - contract

## final analysis
10,000 total peices were minted. I'm really proud of the result and really hope someone takes the time to enjoy not just one piece, but the set as they sit next to each other with their differences and similarities. Below are some examples with a bit of a walk through on each. There is a lot more randomness and complexity going into each and if you want you can take time to review the code here on github. If you would like me to attempt to unravel yours then you can reach out on [Discord](https://discord.gg/HWnrVSBC) or [Twitter](https://twitter.com/mindrash).

### name: d29ya3Byb3RvY29scy5jb20=

---

<p>
    <img style="width:35%;padding:20px;" src="https://img.tofunft.com/image/https%3A%2F%2Fimg.tofunft.com%2Fipfs%2FQmVQhu4q56e5FDB5KcpuFBv4NwTT9dkEXDoCYuoiwoQZtn/720.png" alt="d29ya3Byb3RvY29scy5jb20=" align="right"/>
    This is a lovely red palette from the domain. This one comes with 15 cookies and 139342 bytes to influence the design. 
    This means 3 lines, 2 ellipses, 0 freek ellipse, and 75 characters added. The characters can be seen faintly in the organge, yellow fading out area. The lines worked well in this one bringing down a darker element from top to bottom worrking with the 3 dark blocks in the top row. Love this one.
</p>
<br clear="all"/>
<br clear="all"/>

### name: YnVydW5pc3RhbmJ1bC5jb20=

---

<p>
    <img style="width:35%;padding:20px;" src="https://img.tofunft.com/image/https%3A%2F%2Fimg.tofunft.com%2Fipfs%2FQma2UWBiia9u8qVPPrtuXAhPe6XymV7i4tEgJw2MfNYDwc/720.png" alt="YnVydW5pc3RhbmJ1bC5jb20=" align="right"/>
    This one contracts with the one aboe so well and a huge reason why I love this project. They can be so different, but all still cohesive as a set. This one was influenced by 0 cookies and 174 bytes which means there wasn't much there to speak of. It ended up with 7 lines, 2 ellipses, 0 freak ellipse, and 0 characters added.
</p>
<br clear="all"/>
<br clear="all"/>

### name: d3d3LmVraW5oZG9hbmguY29t

---

<p>
    <img style="width:35%;padding:20px;" src="https://img.tofunft.com/image/https%3A%2F%2Fimg.tofunft.com%2Fipfs%2FQmVwqDrsZUUMpoaPRUMv2eZRMMQ6yN5rr7Y5BCEFY868v6/720.png" alt="d3d3LmVraW5oZG9hbmguY29t" align="right"/>
    Another example of how different they can be and still so relatable. Influeced by 0 cookies and 15326 bytes this one ends up with 5 lines, 2 ellipses, and 0 characters.
</p>
<br clear="all"/>
<br clear="all"/>

### name: c3dpbXdlaWdodHMuY29t

---

<p>
    <img style="width:35%;padding:20px;" src="https://img.tofunft.com/image/https%3A%2F%2Fimg.tofunft.com%2Fipfs%2FQmUxkqmHAWpL8ywNfKZfQtgfziz4JxvxVhcXGe1Vkc2mpW/720.png" alt="c3dpbXdlaWdodHMuY29t" align="right"/>
    This is one came out with the freak ellipse which are the rows of ellipses. In this case it looks to have recieved the standard color key for these. Some with the freak ellipse will have a color key pulled from the foundational color palette. The ellipses here come together has a nice eyeball which is why I sometimes refer to it as the eye because there isn't a better name for it.
</p>

<br clear="all"/>
<br clear="all"/>

---

[Polyscan](https://polygonscan.com/address/0x752cd43b36171a5c49fdbdf74574c6edff439e81) | 
[Discord](https://discord.gg/HWnrVSBC) | 
[Twitter](https://twitter.com/mindrash) | 
[Rarible](https://rarible.com/metadevil-io/items) | 
[PEBKAC.fyi](https://pebkac.fyi) | 
[itsmookie.com](https://itsmookie.com)


