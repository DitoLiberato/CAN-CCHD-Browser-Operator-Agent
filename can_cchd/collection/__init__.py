from can_cchd.collection.adapters.pubmed_adapter import PubMedAdapter
from can_cchd.collection.adapters.europepmc_adapter import EuropePMCAdapter
from can_cchd.collection.adapters.crossref_adapter import CrossrefAdapter
from can_cchd.collection.adapters.openalex_adapter import OpenAlexAdapter
from can_cchd.collection.adapters.semantic_scholar_adapter import SemanticScholarAdapter
from can_cchd.collection.adapters.ris_adapter import RISAdapter


def get_adapter(source_name: str, conn):
    """Factory function — returns the right adapter for a given source name."""
    name = source_name.lower()
    if "pubmed" in name or "medline" in name:
        return PubMedAdapter(conn)
    elif "europe pmc" in name:
        return EuropePMCAdapter(conn)
    elif "crossref" in name:
        return CrossrefAdapter(conn)
    elif "openalex" in name:
        return OpenAlexAdapter(conn)
    elif "semantic scholar" in name:
        return SemanticScholarAdapter(conn)
    else:
        return None  # Manual/unsupported — will use RIS upload
