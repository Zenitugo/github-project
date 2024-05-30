import yaml
import xml.etree.ElementTree as xml_tree

# Function to debug the tree structure
def debug_tree(element, depth=0):
    indent = "  " * depth
    print(f"{indent}Element: {element.tag}, Text type: {type(element.text)}, Text: {element.text}")
    for child in element:
        debug_tree(child, depth + 1)


with open('rss-feed.yml', 'r') as file:
    yaml_data = yaml.safe_load(file)

    rss_element = xml_tree.Element('rss', {

        'xmlns:atom':'http://www.w3.org/2005/Atom', 
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/',
        'xmlns:googleplay':'http://www.google.com/schemas/play-podcasts/1.0', 
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:media':'http://search.yahoo.com/mrss/', 
        'xmlns:podcast':'https://podcastindex.org/namespace/1.0',
        'version':'2.0'})

    channel_element = xml_tree.SubElement(rss_element, 'channel')

    link_prefix = yaml_data['link']
    xml_tree.SubElement(channel_element, 'title').text = str(yaml_data['title'])
    xml_tree.SubElement(channel_element, 'description').text = str(yaml_data['description'])
    xml_tree.SubElement(channel_element, 'copyright').text = str(yaml_data['copyright'])
    xml_tree.SubElement(channel_element, 'language').text = str(yaml_data['language'])
    xml_tree.SubElement(channel_element, 'pubDate').text = str(yaml_data['pubDate'])
    xml_tree.SubElement(channel_element, 'link').text = str(link_prefix)
    xml_tree.SubElement(channel_element, 'lastBuilddate').text = str(yaml_data['lastBuildDate'])
    xml_tree.SubElement(channel_element, 'itunes:link').text = str(yaml_data['link'])
    xml_tree.SubElement(channel_element, 'itunes:image', {'href': yaml_data['image']})
    xml_tree.SubElement(channel_element, 'itunes:type').text = str(yaml_data['itunes:type'])
    xml_tree.SubElement(channel_element, 'itunes:summary').text = str(yaml_data['itunes:summary'])
    xml_tree.SubElement(channel_element, 'itunes:author').text = str(yaml_data['itunes:author'])
    xml_tree.SubElement(channel_element, 'itunes:keyword').text = str(yaml_data['itunes:keyword'])
    xml_tree.SubElement(channel_element, 'itunes:owner').text = str(yaml_data['itunes:owner'])
    xml_tree.SubElement(channel_element, 'itunes:type').text = str(yaml_data['itunes:type'])
    xml_tree.SubElement(channel_element, 'itunes:new-feed-url').text = str(yaml_data['itunes:new-feed-url'])


    for item in yaml_data['item']:
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = str(item['title'])
        xml_tree.SubElement(item_element, 'description').text = str(item['description'])
        xml_tree.SubElement(item_element, 'pubDate').text = str(item['pubDate'])
        xml_tree.SubElement(item_element, 'itunes:author').text = str(item['link'])
        xml_tree.SubElement(item_element, 'link').text = link_prefix

        enclosure = xml_tree.SubElement(item_element, 'enclosure', {
          'url': item['url'],
          'type': 'audio/mpeg',
          'length': item['length']
        })
  

    
    # Debug the tree structure before writing
    debug_tree(rss_element)


     # Write to file 
    output_tree = xml_tree.ElementTree(rss_element)
    output_tree.write('News.xml', encoding='UTF_8', xml_declaration=True)
    
