Hyperledger Indy
================

.. image:: https://raw.githubusercontent.com/hyperledger/indy-node/master/collateral/logos/indy-logo.png

Hyperledger Indy provides tools, libraries, and reusable components for providing digital identities rooted on blockchains or other distributed ledgers so that they are interoperable across administrative domains, applications, and any other silo.

If you are a developer, begin your journey by looking at an Aries Framework such as `Aries Cloud Agent Python <https://aca-py.org>`_ , `Credo JS <https://credo.js.org>`_ or `Aries VCX <https://github.com/hyperledger/aries-vcx>`_

Key Characteristics
-------------------
    - Distributed ledger purpose-built for decentralized identity
    - Correlation-resistant by design
    - DIDs (Decentralized Identifiers) that are globally unique and resolvable (via a ledger) without requiring any centralized resolution authority
    - Pairwise Identifiers create secure, 1:1 relationships between any two entities
    - Verifiable Claims are interoperable format for exchange of digital identity attributes and relationships currently in the standardization pipeline at the W3C
    - Zero Knowledge Proofs which prove that some or all of the data in a set of Claims is true without revealing any additional information, including the identity of the Prover

Our Repositories
-----------------

* Distributed Ledger:

    * `indy-node <https://github.com/hyperledger/indy-node>`_
    * `indy-plenum <https://github.com/hyperledger/indy-plenum>`_

* Client Tools:

    * DEPRECATED: `indy-sdk <https://github.com/hyperledger/indy-sdk>`_
        * Use the so-called Shared Libraries instead:
            * `Indy VDR ledger interface/client <https://github.com/hyperledger/indy-vdr>`_
            * `Aries Askar secure storage <https://github.com/hyperledger/aries-askar>`_
            * `Hyperledger AnonCreds Verifiable Credentials implementation <https://github.com/hyperledger/anoncreds-rs>`_
            * `Indy CLI <https://github.com/hyperledger/indy-cli-rs>`_
    * DEPRECATED: `indy-agent <https://github.com/hyperledger/indy-agent>`_
        * Use one of the Hyperledger Aries Frameworks:
            * `Aries Cloud Agent Python <https://aca-py.org>`_
            * `Credo (formerly Aries Framework JavaScript) <https://credo.js.org>`_
            * `Aries VCX <https://github.com/hyperledger/aries-vcx>`_

* Shared Components:

    * `indy-hipe <https://github.com/hyperledger/indy-hipe>`_
    * DEPRECATED: `indy-crypto <https://github.com/hyperledger/indy-crypto>`_
        * Replaced by:
            * `Indy BLS Signatures <https://github.com/hyperledger/indy-blssignatures-rs>`_
            * `Hyperledger AnonCreds CL Signatures <https://github.com/hyperledger/anoncreds-clsignatures-rs>`_

.. toctree:: 
   :caption: Indy
   :hidden:

   docs.md

