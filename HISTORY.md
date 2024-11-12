# [5.0.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v4.0.4...v5.0.0) (2024-11-12)


### Features

* **centralnic reseller python sdk:** Introducing CentralNic Reseller Python SDK API Connector ([a78900c](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/a78900cd6488f77dbd722fca66f58599eff6348e))


### BREAKING CHANGES

* **centralnic reseller python sdk:** This release deprecates the Hexonet Python SDK and introduces the CentralNic Reseller Python SDK.
- Note: To continue using the Hexonet SDK, please install version 4.0.2 or earlier.

## [4.0.4](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v4.0.3...v4.0.4) (2024-10-21)


### Bug Fixes

* **deps:** update sphinx-rtd-theme requirement from <3,>=1 to >=1,<4 ([f4749f6](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/f4749f6fd34550cc3f7cfe4a1565715c8051c56c))

## [4.0.3](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v4.0.2...v4.0.3) (2024-09-04)


### Bug Fixes

* **deps:** update sphinx requirement from <8,>=3 to >=3,<9 ([71f6e91](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/71f6e9111298285b3b11c898862e4c5154317855))
* **deps:** update sphinxcontrib-websupport requirement ([b00095c](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/b00095c5019b43b66df22593a375703cc5362ad8))

## [4.0.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v4.0.1...v4.0.2) (2023-11-09)


### Bug Fixes

* **README:** remove 4.0.1 duplicates and test releasing again ([bfb1057](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/bfb10577bdbcbb8e8e613e5facf435f5928c92e9))

## [4.0.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v4.0.0...v4.0.1) (2023-11-09)

### Bug Fixes

* **developmentguide.rst:** Cleanup of setup.cfg and updated with pyproject.toml ([8895d54](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/8895d54757f9737d17ddeefd4af9e25b7cc0480f))
* **github actions:** extend release process ([cf63206](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/cf63206e9986e768a1d1cfde65ab4d08b93840f6))
* **github actions:** extend release process permissions ([c7ef2df](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/c7ef2df2604a1a1defc8734ead3bbffcbd895940))
* **github actions:** last tryout ([31bf7c7](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/31bf7c7d4dba358b9be63bbde0175f6306675635))
* **github actions:** playing with release process ([ad245d0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/ad245d053295f4db1c3a381ead4d39d3f13dc17e))
* **pyproject.toml:** Cleanup of setup.py in favour of pyproject.toml ([52f05a8](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/52f05a8252e3e1e6d0e2b05187199eee13e646fc))
* **releaserc.json:** included pyproject.toml in release git assets ([f54a85e](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/f54a85e23b5553df63e046661a9cd58f4e8f5d9e))
* **sphinx:** upgraded to latest version and condition syntax fix ([0f8e4f3](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/0f8e4f3f6af999b77878615c560ad88a2eaeda1f))

# [4.0.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.8.4...v4.0.0) (2022-06-08)

### chore

- **dep-bump:** upgrade dev-deps and test release process ([33f4309](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/33f4309e44eb141e6577d5199f69bb220c8d94bb))

### BREAKING CHANGES

- **dep-bump:** semantic-release v19

## [3.8.4](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.8.3...v3.8.4) (2022-04-01)

### Bug Fixes

- **dep bump:** trigger new version as of twine 4.0 ([abd3472](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/abd34724f36574cb5119b0ab9f13c8139186a206))

## [3.8.3](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.8.2...v3.8.3) (2022-03-23)

### Bug Fixes

- **ot&e:** url updated for OT&E environment ([6bdebc8](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/6bdebc8427cb7f55495fc831f7a42a5baa7e9ae8))

## [3.8.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.8.1...v3.8.2) (2021-01-22)

### Bug Fixes

- **ci:** migration from Travis CI to github actions ([d74edcd](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/d74edcd5dbfaf010d2fc91f2525dcc4c65955b79))
- **ci:** missing replacement of m2r with m2r2 in docs/conf.py ([4a1ec74](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/4a1ec7416a66a0cafb9b710b71687322ab9d3600))
- **ci:** replace m2r (abandoned) with m2r2 ([1e048c5](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/1e048c5b017fd7d476b4f883c714e24bb70e0b3a))
- **test & coverage:** reviewed dependency management, coverage reporting and configs ([2bd868a](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/2bd868a9c40cb9d5dbb48328e4c1344702d2f022))

## [3.8.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.8.0...v3.8.1) (2020-05-23)

### Bug Fixes

- **apiclient:** fixed empty ConvertIDN request ([8d4e96d](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/8d4e96df2600069fb78d2c098a8219a4fed730cc))

# [3.8.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.7.0...v3.8.0) (2020-05-07)

### Features

- **logger:** possibility to override debug mode's default logging mechanism ([944d9de](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/944d9de24e9f391511ace3ce582bb49b0d8be347))

# [3.7.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.6.0...v3.7.0) (2020-05-07)

### Features

- **response:** possibility of placeholder vars in standard responses to improve error details ([393f20c](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/393f20cd48dbb5e88a08114eca4b972f395ce805))

# [3.6.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.5.1...v3.6.0) (2020-05-07)

### Features

- **apiclient:** allow to specify additional libraries via setUserAgent ([3100656](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/310065612ac70376c93d93dc6fecb257bd6340b1))

## [3.5.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.5.0...v3.5.1) (2020-04-30)

### Bug Fixes

- **security:** replace passwords whereever they could be used for output ([9215b87](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/9215b87e5353cbd2c9ce43c24099b1732104a879))

# [3.5.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.4.2...v3.5.0) (2020-04-30)

### Features

- **response:** added getCommandPlain (getting used command in plain text) ([2efab17](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/2efab17a99402a849ad6ef712458b32a9b4594b9))

## [3.4.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.4.1...v3.4.2) (2020-04-29)

### Bug Fixes

- **responsetemplatemanager:** fixed namingconventions self vs. cls ([b52b22d](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/b52b22d4a51c1a498870bf5b0e9a9ab73ab8ddbd))

## [3.4.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.4.0...v3.4.1) (2020-04-29)

### Bug Fixes

- **messaging:** return a specific error template if API response' code or description are missing ([7cd33b4](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/7cd33b4cae237ae1657599a1f662ec69388971a3))

# [3.4.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.3.0...v3.4.0) (2020-04-29)

### Features

- **apiclient:** support the `High Performance Proxy Setup`. see README.md ([d66d495](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/d66d495b0033bb9e6adcf7e9b7adb27c4eda63dd))

# [3.3.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.2.2...v3.3.0) (2020-04-29)

### Features

- **apiclient:** automatic IDN conversion of API command parameters to punycode ([6562f26](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/6562f26c8741efa54bcf293331b8a6687b198828))

## [3.2.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.2.1...v3.2.2) (2020-03-11)

### Bug Fixes

- **travis:** remove branch verification in updateVersion.sh as releasing happens on master ([4eb327e](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/4eb327e85e22f78d24048edaae3a175f74b3f314))

## [3.2.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.2.0...v3.2.1) (2020-03-11)

### Bug Fixes

- **travis:** fixed node env usage in ci/release process ([6e8f9e0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/6e8f9e0ee483e3d3d053805982e1d14647a07cc7))

# [3.2.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.1.4...v3.2.0) (2020-03-11)

### Features

- **apiclient:** support bulk parameters through nested array in API command ([1e4b8e7](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/1e4b8e76f0f695e5e2780619b26aa0017b419b46))

## [3.1.4](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.1.3...v3.1.4) (2019-10-04)

### Bug Fixes

- **responsetemplate/mgr:** improve description for `423 Empty API response` [HM-577] ([7bbcee9](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/7bbcee9))
- **responsetemplate/mgr:** pep8 review of response description usage ([1410e58](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/1410e58))

## [3.1.3](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.1.2...v3.1.3) (2019-09-24)

### Bug Fixes

- **Travis:** fixed pip calls ([479cd06](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/479cd06))
- **Travis:** upgrade packages in build ([3756193](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/3756193))

## [3.1.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.1.1...v3.1.2) (2019-09-19)

### Bug Fixes

- **release process:** migrate configuration ([9fcd7d1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/9fcd7d1))

## [3.1.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.1.0...v3.1.1) (2019-08-16)

### Bug Fixes

- **APIClient:** update default SDK url ([758bf13](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/758bf13))

# [3.1.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.0.2...v3.1.0) (2019-04-16)

### Features

- **responsetemplate:** add isPending method ([c429972](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/c429972))

## [3.0.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.0.1...v3.0.2) (2019-04-04)

### Bug Fixes

- **APIClient:** return APIClient instance in setUserAgent method ([2169891](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/2169891))

## [3.0.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v3.0.0...v3.0.1) (2019-04-01)

### Bug Fixes

- **docs:** remove python 2 documentation from docs ([81a4586](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/81a4586))

# [3.0.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v2.1.2...v3.0.0) (2019-04-01)

### Code Refactoring

- **pkg:** python 2 support removal ([11351aa](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/11351aa))

### BREAKING CHANGES

- **pkg:** drop python 2 support

## [2.1.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v2.1.1...v2.1.2) (2019-04-01)

### Bug Fixes

- **apiclient:** fix usage of user agent header field ([bbd9095](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/bbd9095))

## [2.1.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v2.1.0...v2.1.1) (2019-03-29)

### Bug Fixes

- **apiclient:** fix useragent string. missing semicolon ([8161b41](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/8161b41))

# [2.1.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v2.0.2...v2.1.0) (2019-03-29)

### Features

- **apiclient:** review useragent support ([4b4d9a7](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/4b4d9a7))

## [2.0.2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/compare/v2.0.1...v2.0.2) (2019-03-06)

### Bug Fixes

- **response:** remove deprecated debug outputs ([70dbe7e](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk/commit/70dbe7e))

## [2.0.1](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk.git/compare/v2.0.0...v2.0.1) (2018-10-31)

### Bug Fixes

- **releasing:** moved travis deploy step into semantic release ([c1a3415](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk.git/commit/c1a3415))

# [2.0.0](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk.git/compare/v1.2.7...v2.0.0) (2018-10-31)

### Bug Fixes

- **semantic-release:** missing setup ([f100c3e](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk.git/commit/f100c3e))

### Code Refactoring

- **pkg:** migrate to cross-SDK UML diagram ([52a78a2](https://github.com/centralnicgroup-opensource/rtldev-middleware-python-sdk.git/commit/52a78a2))

### BREAKING CHANGES

- **pkg:** rewrite from scratch to align the structure of our SDKs; downward incompatible
